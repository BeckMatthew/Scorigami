import polars as pl
import numpy as np
import fastexcel
import math

# Download xlsx file containing scorigami occurences that was used in Moyer et al's paper


# Importing Dataset from nflreadpy
nflScores = pl.read_excel("EveryScorigami.xlsx")
scorigami = nflScores.filter(pl.col('New Scorigami?')=="true").select("PtsW","PtsL","Season").drop_nulls()

def isScorigami(score1,score2,season):
    ptsW = max(score1,score2)
    ptsL = min(score1,score2)
    if ptsW in scorigami.filter(pl.col('Season')<season)['PtsW']:
        if ptsL in scorigami.filter((pl.col('Season')<season) & (pl.col('PtsW') == ptsW))['PtsL']:
            return False
        else:
            return True
    else:
        return True
