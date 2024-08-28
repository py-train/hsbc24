import matplotlib.pyplot as plt
import numpy as np

def plot_svc_decision_function(X, clf, ax=None):
    """Plot the decision function for a 2D SVC"""
    if ax is None:
        ax = plt.gca()
    x = np.linspace(plt.xlim()[0], plt.xlim()[1], 30)
    y = np.linspace(plt.ylim()[0], plt.ylim()[1], 30)
    Y, X = np.meshgrid(y, x)
    P = np.zeros_like(X)
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            P[i, j] = clf.decision_function([[xi, yj]])
    # plot the margins
    ax.contour(X, Y, P, colors='k',
               levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'])
    return P


def plot_support(clf, ax=None):
    'Mark the support vectors of the SVC model as scatter points above the decision function contour'
    if ax is None:
        ax = plt.gca()
    ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
        s=200, facecolors='none', edgecolors='black');
    
    
