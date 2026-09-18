from __future__ import annotations
import math
from typing import Tuple, Dict, Any
import numpy as np


class NaiveBayesGaussian:
    """
    Gaussian Naive Bayes for continuous features.
    Uses variance smoothing to stabilize likelihoods.
    """
    def __init__(self, var_smoothing: float = 1e-9):
        self.var_smoothing = var_smoothing
        self.classes_: np.ndarray | None = None
        self.class_prior_log_: Dict[Any, float] = {}
        self.mean_: Dict[Any, np.ndarray] = {}
        self.var_: Dict[Any, np.ndarray] = {}

    def fit(self, X: np.ndarray, y: np.ndarray) -> "NaiveBayesGaussian":
        X = np.asarray(X, dtype=float)
        y = np.asarray(y)
        self.classes_ = np.unique(y)

        # Class priors
        for c in self.classes_:
            Xc = X[y == c]
            self.class_prior_log_[c] = math.log(len(Xc) / len(X))
            mu = Xc.mean(axis=0)
            var = Xc.var(axis=0) + self.var_smoothing
            self.mean_[c] = mu
                        self.var_[c] = var
        return self

    def _log_gaussian_likelihood(self, x: np.ndarray, c: Any) -> float:
        mu = self.mean_[c]
        var = self.var_[c]
        # Compute sum over features of log N(x|mu,var)
        # log-likelihood per feature
        return -0.5 * (np.log(2 * np.pi * var)).sum() - 0.5 * (((x - mu) ** 2) / var).sum()

    def _joint_log_likelihood(self, X: np.ndarray) -> np.ndarray:
        scores = []
        for x in X:
            row = []
            for c in self.classes_:
                row.append(self.class_prior_log_[c] + self._log_gaussian_likelihood(x, c))
            scores.append(row)
        return np.array(scores)

    def predict(self, X: np.ndarray) -> np.ndarray:
        X = np.asarray(X, dtype=float)
        jll = self._joint_log_likelihood(X)
        idx = jll.argmax(axis=1)
        return self.classes_[idx]

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        jll = self._joint_log_likelihood(np.asarray(X, dtype=float))
        # softmax
        jll -= jll.max(axis=1, keepdims=True)
        probs = np.exp(jll)
        probs /= probs.sum(axis=1, keepdims=True)
        return probs
        class NaiveBayesMultinomial:
    """
    Multinomial Naive Bayes for non-negative count features.
    Uses Laplace (add-alpha) smoothing.
    """
    def __init__(self, alpha: float = 1.0):
        if alpha < 0:
            raise ValueError("alpha must be >= 0")
        self.alpha = alpha
        self.classes_: np.ndarray | None = None
        self.class_prior_log_: Dict[Any, float] = {}
        self.feature_log_prob_: Dict[Any, np.ndarray] = {}

    def fit(self, X: np.ndarray, y: np.ndarray) -> "NaiveBayesMultinomial":
        X = np.asarray(X, dtype=float)
        if (X < 0).any():
            raise ValueError("Multinomial NB requires non-negative counts.")
        y = np.asarray(y)
        self.classes_ = np.unique(y)

        # Priors
        for c in self.classes_:
            Xc = X[y == c]
            self.class_prior_log_[c] = math.log(len(Xc) / len(X))

            # Feature likelihoods with Laplace smoothing
            counts = Xc.sum(axis=0)  # total count per feature for class c
            total = counts.sum()
            probs = (counts + self.alpha) / (total + self.alpha * X.shape[1])
            self.feature_log_prob_[c] = np.log(probs)
