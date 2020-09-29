from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import make_scorer, matthews_corrcoef

# define matthews score to use in cross validation scoring
matthews = make_scorer(matthews_corrcoef)

def score_this(pipe, X, y, n_splits=5):
    """Prints cross validated classification metrics for any 
       given classification pipeline using Stratified KFold.
    Parameters:
    -----------
    pipe: pipeline object
        Classification pipeline
    X: pandas.Dataframe
        Predictive variables(features)
    y: pandas.Series
        Predicted variables(target)
    n_splits: number of folds(optional)
        Default is 5
    Returns:
    --------
    None
    """
    skfold = StratifiedKFold(n_splits, random_state=43)
    print(f"\nAccuracy: {cross_val_score(pipe, X, y, scoring='accuracy', cv=skfold).mean():.6f}"
          f"\nMatthews: {cross_val_score(pipe, X, y, scoring=matthews, cv=skfold).mean():.6f}"
          f"\nF1: {cross_val_score(pipe, X, y, scoring='f1', cv=skfold).mean():.6f}"
         )
    return