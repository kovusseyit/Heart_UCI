from sklearn.metrics import make_scorer, matthews_corrcoef

# define matthews score to use in cross validation scoring
matthews = make_scorer(matthews_corrcoef)