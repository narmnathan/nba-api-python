# Loading gamelogs


```python
from load import run
run('Jayson Tatum BOS vs. LAC 24.5 REBS')
# enter full name, player team, court, opposing team, fantasy value and type
```

    Gamelogs successfully loaded for Jayson Tatum


# Accessing gamelogs



```python
from manager import CSV
player = CSV.gamelog['player']
team = CSV.gamelog['team']
opponent = CSV.gamelog['opp']

player.head() # show player gamelogs
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SEASON_ID</th>
      <th>Player_ID</th>
      <th>Game_ID</th>
      <th>GAME_DATE</th>
      <th>MATCHUP</th>
      <th>WL</th>
      <th>MIN</th>
      <th>FGM</th>
      <th>FGA</th>
      <th>FG_PCT</th>
      <th>...</th>
      <th>DREB</th>
      <th>REB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>PLUS_MINUS</th>
      <th>VIDEO_AVAILABLE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>22022</td>
      <td>1628369</td>
      <td>22201206</td>
      <td>APR 07, 2023</td>
      <td>BOS vs. TOR</td>
      <td>W</td>
      <td>20</td>
      <td>7</td>
      <td>12</td>
      <td>0.583</td>
      <td>...</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>2</td>
      <td>21</td>
      <td>23</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>22022</td>
      <td>1628369</td>
      <td>22201181</td>
      <td>APR 04, 2023</td>
      <td>BOS @ PHI</td>
      <td>L</td>
      <td>38</td>
      <td>7</td>
      <td>20</td>
      <td>0.350</td>
      <td>...</td>
      <td>5</td>
      <td>6</td>
      <td>6</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>19</td>
      <td>-13</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>22022</td>
      <td>1628369</td>
      <td>22201152</td>
      <td>MAR 31, 2023</td>
      <td>BOS vs. UTA</td>
      <td>W</td>
      <td>36</td>
      <td>12</td>
      <td>17</td>
      <td>0.706</td>
      <td>...</td>
      <td>10</td>
      <td>11</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>39</td>
      <td>7</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>22022</td>
      <td>1628369</td>
      <td>22201146</td>
      <td>MAR 30, 2023</td>
      <td>BOS @ MIL</td>
      <td>W</td>
      <td>31</td>
      <td>12</td>
      <td>18</td>
      <td>0.667</td>
      <td>...</td>
      <td>7</td>
      <td>8</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>40</td>
      <td>36</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>22022</td>
      <td>1628369</td>
      <td>22201130</td>
      <td>MAR 28, 2023</td>
      <td>BOS @ WAS</td>
      <td>L</td>
      <td>32</td>
      <td>11</td>
      <td>19</td>
      <td>0.579</td>
      <td>...</td>
      <td>9</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>28</td>
      <td>-10</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 27 columns</p>
</div>



# Filtering gamelogs
Gamelogs can be filtered by:
- Home/away
- Opposing team
- Last n games
- Minimum/maximum minutes played
- Games without a teammate playing 


```python
import filters
from manager import Filtered
# filtering for games played at home
filters.court('HOME')
last = Filtered.player['court']

last.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SEASON_ID</th>
      <th>Player_ID</th>
      <th>Game_ID</th>
      <th>GAME_DATE</th>
      <th>MATCHUP</th>
      <th>WL</th>
      <th>MIN</th>
      <th>FGM</th>
      <th>FGA</th>
      <th>FG_PCT</th>
      <th>...</th>
      <th>DREB</th>
      <th>REB</th>
      <th>AST</th>
      <th>STL</th>
      <th>BLK</th>
      <th>TOV</th>
      <th>PF</th>
      <th>PTS</th>
      <th>PLUS_MINUS</th>
      <th>VIDEO_AVAILABLE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>22022</td>
      <td>1628369</td>
      <td>22201206</td>
      <td>APR 07, 2023</td>
      <td>BOS vs. TOR</td>
      <td>W</td>
      <td>20</td>
      <td>7</td>
      <td>12</td>
      <td>0.583</td>
      <td>...</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>2</td>
      <td>21</td>
      <td>23</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>22022</td>
      <td>1628369</td>
      <td>22201152</td>
      <td>MAR 31, 2023</td>
      <td>BOS vs. UTA</td>
      <td>W</td>
      <td>36</td>
      <td>12</td>
      <td>17</td>
      <td>0.706</td>
      <td>...</td>
      <td>10</td>
      <td>11</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>39</td>
      <td>7</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>22022</td>
      <td>1628369</td>
      <td>22201097</td>
      <td>MAR 24, 2023</td>
      <td>BOS vs. IND</td>
      <td>W</td>
      <td>32</td>
      <td>13</td>
      <td>24</td>
      <td>0.542</td>
      <td>...</td>
      <td>7</td>
      <td>7</td>
      <td>2</td>
      <td>2</td>
      <td>0</td>
      <td>6</td>
      <td>3</td>
      <td>34</td>
      <td>23</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>22022</td>
      <td>1628369</td>
      <td>22200986</td>
      <td>MAR 08, 2023</td>
      <td>BOS vs. POR</td>
      <td>W</td>
      <td>31</td>
      <td>11</td>
      <td>17</td>
      <td>0.647</td>
      <td>...</td>
      <td>6</td>
      <td>7</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>30</td>
      <td>21</td>
      <td>1</td>
    </tr>
    <tr>
      <th>13</th>
      <td>22022</td>
      <td>1628369</td>
      <td>22200969</td>
      <td>MAR 05, 2023</td>
      <td>BOS vs. NYK</td>
      <td>L</td>
      <td>49</td>
      <td>12</td>
      <td>30</td>
      <td>0.400</td>
      <td>...</td>
      <td>9</td>
      <td>11</td>
      <td>6</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>2</td>
      <td>40</td>
      <td>4</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 27 columns</p>
</div>



# Retrieving statistics
Available statistics:
1. PTS, REB, AST, BLK, TOV, PF
2. REB, OREB, DREB, OREB_RATIO, DREB_RATIO
3. FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FG3_RATIO, FTM, FTA, FT_PCT
4. AST%, AST/TO, eFG%, TSA, TOV%, TS%, USG%
5. OREB%, DREB%, BLK%, STL%



```python
import stats
# showing PTS, REB, AST, BLK, TOV, and PF for games played at home
stats.change('COURT')
stats.basic()
```

                  
    PTS  30.067568
    REB   8.770270
    AST   4.621622
    BLK   0.689189
    TOV   2.878378
    PF    2.162162

