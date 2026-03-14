import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def compare_fradulent_vs_not(df, column, top_n=10):
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    fraudulent = df['fraudulent'] == 't'
    not_fraudulent = df['fraudulent'] == 'f'

    df.loc[fraudulent, column].value_counts().nlargest(top_n).plot(kind='barh', ax=axes[0], color='slategrey')
    axes[0].set_title(f'Fraudulent - Top {top_n}')
    axes[0].invert_yaxis()

    df.loc[not_fraudulent, column].value_counts().nlargest(top_n).plot(kind='barh', ax=axes[1], color='steelblue')
    axes[1].set_title(f'Not Fraudulent - Top {top_n}')
    axes[1].invert_yaxis()

    plt.suptitle(column, fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.show()
