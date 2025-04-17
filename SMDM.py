{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import scipy.stats as stats\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import math\n",
    "import os\n",
    "from   scipy.stats               import ttest_1samp, ttest_ind\n",
    "from   scipy.stats               import ttest_rel\n",
    "\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Problem #1\n",
    "\n",
    "Problem Statement:\n",
    "\n",
    "A wholesale distributor operating in different regions of Portugal has information on annual spending of several items in their stores across different regions and channels. The data consists of 440 large retailers’ annual spending on 6 different varieties of products in 3 different regions (Lisbon, Oporto, Other) and across different sales channel (Hotel, Retail)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1.1 Use methods of descriptive statistics to summarize data. Which Region and which Channel spent the most? Which Region and which Channel spent the least?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "WS = pd.read_csv(\"Wholesale Customer.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Buyer/Spender</th>\n",
       "      <th>Channel</th>\n",
       "      <th>Region</th>\n",
       "      <th>Fresh</th>\n",
       "      <th>Milk</th>\n",
       "      <th>Grocery</th>\n",
       "      <th>Frozen</th>\n",
       "      <th>Detergents_Paper</th>\n",
       "      <th>Delicatessen</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Retail</td>\n",
       "      <td>Other</td>\n",
       "      <td>12669</td>\n",
       "      <td>9656</td>\n",
       "      <td>7561</td>\n",
       "      <td>214</td>\n",
       "      <td>2674</td>\n",
       "      <td>1338</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Retail</td>\n",
       "      <td>Other</td>\n",
       "      <td>7057</td>\n",
       "      <td>9810</td>\n",
       "      <td>9568</td>\n",
       "      <td>1762</td>\n",
       "      <td>3293</td>\n",
       "      <td>1776</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Retail</td>\n",
       "      <td>Other</td>\n",
       "      <td>6353</td>\n",
       "      <td>8808</td>\n",
       "      <td>7684</td>\n",
       "      <td>2405</td>\n",
       "      <td>3516</td>\n",
       "      <td>7844</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Hotel</td>\n",
       "      <td>Other</td>\n",
       "      <td>13265</td>\n",
       "      <td>1196</td>\n",
       "      <td>4221</td>\n",
       "      <td>6404</td>\n",
       "      <td>507</td>\n",
       "      <td>1788</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Retail</td>\n",
       "      <td>Other</td>\n",
       "      <td>22615</td>\n",
       "      <td>5410</td>\n",
       "      <td>7198</td>\n",
       "      <td>3915</td>\n",
       "      <td>1777</td>\n",
       "      <td>5185</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Buyer/Spender Channel Region  Fresh  Milk  Grocery  Frozen  \\\n",
       "0              1  Retail  Other  12669  9656     7561     214   \n",
       "1              2  Retail  Other   7057  9810     9568    1762   \n",
       "2              3  Retail  Other   6353  8808     7684    2405   \n",
       "3              4   Hotel  Other  13265  1196     4221    6404   \n",
       "4              5  Retail  Other  22615  5410     7198    3915   \n",
       "\n",
       "   Detergents_Paper  Delicatessen  \n",
       "0              2674          1338  \n",
       "1              3293          1776  \n",
       "2              3516          7844  \n",
       "3               507          1788  \n",
       "4              1777          5185  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "WS.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Buyer/Spender       0\n",
       "Channel             0\n",
       "Region              0\n",
       "Fresh               0\n",
       "Milk                0\n",
       "Grocery             0\n",
       "Frozen              0\n",
       "Detergents_Paper    0\n",
       "Delicatessen        0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "WS.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Buyer/Spender         220.500000\n",
       "Fresh               12000.297727\n",
       "Milk                 5796.265909\n",
       "Grocery              7951.277273\n",
       "Frozen               3071.931818\n",
       "Detergents_Paper     2881.493182\n",
       "Delicatessen         1524.870455\n",
       "dtype: float64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "WS.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Buyer/Spender</th>\n",
       "      <td>440.0</td>\n",
       "      <td>220.500000</td>\n",
       "      <td>127.161315</td>\n",
       "      <td>1.0</td>\n",
       "      <td>110.75</td>\n",
       "      <td>220.5</td>\n",
       "      <td>330.25</td>\n",
       "      <td>440.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fresh</th>\n",
       "      <td>440.0</td>\n",
       "      <td>12000.297727</td>\n",
       "      <td>12647.328865</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3127.75</td>\n",
       "      <td>8504.0</td>\n",
       "      <td>16933.75</td>\n",
       "      <td>112151.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Milk</th>\n",
       "      <td>440.0</td>\n",
       "      <td>5796.265909</td>\n",
       "      <td>7380.377175</td>\n",
       "      <td>55.0</td>\n",
       "      <td>1533.00</td>\n",
       "      <td>3627.0</td>\n",
       "      <td>7190.25</td>\n",
       "      <td>73498.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Grocery</th>\n",
       "      <td>440.0</td>\n",
       "      <td>7951.277273</td>\n",
       "      <td>9503.162829</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2153.00</td>\n",
       "      <td>4755.5</td>\n",
       "      <td>10655.75</td>\n",
       "      <td>92780.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Frozen</th>\n",
       "      <td>440.0</td>\n",
       "      <td>3071.931818</td>\n",
       "      <td>4854.673333</td>\n",
       "      <td>25.0</td>\n",
       "      <td>742.25</td>\n",
       "      <td>1526.0</td>\n",
       "      <td>3554.25</td>\n",
       "      <td>60869.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Detergents_Paper</th>\n",
       "      <td>440.0</td>\n",
       "      <td>2881.493182</td>\n",
       "      <td>4767.854448</td>\n",
       "      <td>3.0</td>\n",
       "      <td>256.75</td>\n",
       "      <td>816.5</td>\n",
       "      <td>3922.00</td>\n",
       "      <td>40827.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Delicatessen</th>\n",
       "      <td>440.0</td>\n",
       "      <td>1524.870455</td>\n",
       "      <td>2820.105937</td>\n",
       "      <td>3.0</td>\n",
       "      <td>408.25</td>\n",
       "      <td>965.5</td>\n",
       "      <td>1820.25</td>\n",
       "      <td>47943.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  count          mean           std   min      25%     50%  \\\n",
       "Buyer/Spender     440.0    220.500000    127.161315   1.0   110.75   220.5   \n",
       "Fresh             440.0  12000.297727  12647.328865   3.0  3127.75  8504.0   \n",
       "Milk              440.0   5796.265909   7380.377175  55.0  1533.00  3627.0   \n",
       "Grocery           440.0   7951.277273   9503.162829   3.0  2153.00  4755.5   \n",
       "Frozen            440.0   3071.931818   4854.673333  25.0   742.25  1526.0   \n",
       "Detergents_Paper  440.0   2881.493182   4767.854448   3.0   256.75   816.5   \n",
       "Delicatessen      440.0   1524.870455   2820.105937   3.0   408.25   965.5   \n",
       "\n",
       "                       75%       max  \n",
       "Buyer/Spender       330.25     440.0  \n",
       "Fresh             16933.75  112151.0  \n",
       "Milk               7190.25   73498.0  \n",
       "Grocery           10655.75   92780.0  \n",
       "Frozen             3554.25   60869.0  \n",
       "Detergents_Paper   3922.00   40827.0  \n",
       "Delicatessen       1820.25   47943.0  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "WS.describe().T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 440 entries, 0 to 439\n",
      "Data columns (total 9 columns):\n",
      " #   Column            Non-Null Count  Dtype \n",
      "---  ------            --------------  ----- \n",
      " 0   Buyer/Spender     440 non-null    int64 \n",
      " 1   Channel           440 non-null    object\n",
      " 2   Region            440 non-null    object\n",
      " 3   Fresh             440 non-null    int64 \n",
      " 4   Milk              440 non-null    int64 \n",
      " 5   Grocery           440 non-null    int64 \n",
      " 6   Frozen            440 non-null    int64 \n",
      " 7   Detergents_Paper  440 non-null    int64 \n",
      " 8   Delicatessen      440 non-null    int64 \n",
      "dtypes: int64(7), object(2)\n",
      "memory usage: 31.1+ KB\n"
     ]
    }
   ],
   "source": [
    "WS.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1.1.1 Data Summary : \n",
    "\n",
    "  * The given dataset consits of 440 entires and 9 columns. \n",
    "  * The dataset consits of no null values and is complete.\n",
    "  * There are two Channels of sales \"Retail\", \"Hotel\" spread across three Regions \"Lisbon\",\"Porto\",\"Others\"\n",
    "  * On an average, the max amount of money spent by clients is on \"Fresh\" and the min amount of spending is on \"Delicatessen\"     "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Channel\n",
       "Hotel     298\n",
       "Retail    142\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "WS.value_counts(\"Channel\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(WS[\"Channel\"])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Region\n",
       "Other     316\n",
       "Lisbon     77\n",
       "Oporto     47\n",
       "dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "WS.value_counts(\"Region\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(WS[\"Region\"])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "WS[\"Total\"] = WS[\"Fresh\"] + WS[\"Milk\"] + WS[\"Grocery\"] + WS [\"Frozen\"] + WS[\"Detergents_Paper\"] + WS[\"Delicatessen\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Buyer/Spender</th>\n",
       "      <th>Fresh</th>\n",
       "      <th>Milk</th>\n",
       "      <th>Grocery</th>\n",
       "      <th>Frozen</th>\n",
       "      <th>Detergents_Paper</th>\n",
       "      <th>Delicatessen</th>\n",
       "      <th>Total</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Region</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Lisbon</th>\n",
       "      <td>18095</td>\n",
       "      <td>854833</td>\n",
       "      <td>422454</td>\n",
       "      <td>570037</td>\n",
       "      <td>231026</td>\n",
       "      <td>204136</td>\n",
       "      <td>104327</td>\n",
       "      <td>2386813</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Oporto</th>\n",
       "      <td>14899</td>\n",
       "      <td>464721</td>\n",
       "      <td>239144</td>\n",
       "      <td>433274</td>\n",
       "      <td>190132</td>\n",
       "      <td>173311</td>\n",
       "      <td>54506</td>\n",
       "      <td>1555088</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Other</th>\n",
       "      <td>64026</td>\n",
       "      <td>3960577</td>\n",
       "      <td>1888759</td>\n",
       "      <td>2495251</td>\n",
       "      <td>930492</td>\n",
       "      <td>890410</td>\n",
       "      <td>512110</td>\n",
       "      <td>10677599</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Buyer/Spender    Fresh     Milk  Grocery  Frozen  Detergents_Paper  \\\n",
       "Region                                                                       \n",
       "Lisbon          18095   854833   422454   570037  231026            204136   \n",
       "Oporto          14899   464721   239144   433274  190132            173311   \n",
       "Other           64026  3960577  1888759  2495251  930492            890410   \n",
       "\n",
       "        Delicatessen     Total  \n",
       "Region                          \n",
       "Lisbon        104327   2386813  \n",
       "Oporto         54506   1555088  \n",
       "Other         512110  10677599  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "WS.groupby('Region').sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Buyer/Spender</th>\n",
       "      <th>Fresh</th>\n",
       "      <th>Milk</th>\n",
       "      <th>Grocery</th>\n",
       "      <th>Frozen</th>\n",
       "      <th>Detergents_Paper</th>\n",
       "      <th>Delicatessen</th>\n",
       "      <th>Total</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Channel</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Hotel</th>\n",
       "      <td>71034</td>\n",
       "      <td>4015717</td>\n",
       "      <td>1028614</td>\n",
       "      <td>1180717</td>\n",
       "      <td>1116979</td>\n",
       "      <td>235587</td>\n",
       "      <td>421955</td>\n",
       "      <td>7999569</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Retail</th>\n",
       "      <td>25986</td>\n",
       "      <td>1264414</td>\n",
       "      <td>1521743</td>\n",
       "      <td>2317845</td>\n",
       "      <td>234671</td>\n",
       "      <td>1032270</td>\n",
       "      <td>248988</td>\n",
       "      <td>6619931</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Buyer/Spender    Fresh     Milk  Grocery   Frozen  Detergents_Paper  \\\n",
       "Channel                                                                        \n",
       "Hotel            71034  4015717  1028614  1180717  1116979            235587   \n",
       "Retail           25986  1264414  1521743  2317845   234671           1032270   \n",
       "\n",
       "         Delicatessen    Total  \n",
       "Channel                         \n",
       "Hotel          421955  7999569  \n",
       "Retail         248988  6619931  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "WS.groupby('Channel').sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1.1.2 , 1.1.3 Client Spending: \n",
    "\n",
    "  * From the given dataset we can see that the distibutor has clients who are in Hotels who spend more as compared to Retail clients \n",
    "  * We can also find out that regions outside of Lisbon and Oporto contribute the highest in spending, Oporto having spent the   least"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1.2 There are 6 different varieties of items that are considered. Describe and comment/explain all the varieties across Region and Channel? Provide a detailed justification for your answer."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "WS_var = WS.drop([\"Buyer/Spender\", \"Total\",\"Channel\"], axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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viCTB7n1+lwplUl0aQbVJ7q6h1JKpZbebCillOqIZkgppTKRRhSUUkqpDKI3HUoppbqigxdKqUyiQSnVJ9rpKaVUaul5VymlVFd08EIplUk0KKWUUg7jdrs59thjOeqoo/j3f/93amtru9z/pZdeYs2aNYd93b/97W88/vjjAHzzm99k5syZiWiuSjG92VBKaT+huqKDF0qpTOontNC56hX7pkg7PdXfXfujn7D/QOIW3Bk8qJS//vHOLvfJy8tjxYoVAFx++eXce++9/OxnP+t0/5deeokZM2YwZcqULl/3qquu6nF7lXPoAhNKOZP2E8ppdPBCKWfRfqJrGpRSfaKdnurv9h+oZvOQMxP3gvve6dHup556Kp9++ikAmzdv5pprrqGyspL8/HwefPBBqqureeWVV3jnnXf4zW9+w6xZs5g/fz4PPPAAwWCQiRMn8sQTT5Cfn89tt91GYWEhN9xwQ+Lej0oZOxil512lnEX7CeUUOmihlDNpP9E1nb6nekVH7JVKvkgkwrx587jgggsAuPLKK7nnnnv4+OOPueuuu/j+97/PaaedxgUXXMCdd97JihUrmDBhAl/96lf56KOP+OSTT/jMZz7Dww8/nOZ3ohJBz7tKqfa0n1Ad0cELpZQtE/oJzZRSvWJ3dtrpKZV4LS0tHHvssWzbto0TTjiBc845h8bGRj744AMuvvji1v0CgUCHx69atYpbbrmF2tpaGhsbOffcc1PVdJVEmimllLJpP6G6ooMXSqlM6ic0U0oppRzGngO+fft2gsEg9957L9FolJKSElasWNH6tXbt2g6P/+Y3v8lf//pXVq5cya233orf70/xO1DJoDcZSimb9hOqIzpooZSyZVI/oUEp1Sd6k6RU8gwYMIC7776bu+66i7y8PMaNG8fzzz8PxD57n3zyCQBFRUU0NDS0HtfQ0MCwYcMIhUI89dRTaWm7Sjw93yql2tN+QnVE+wullC0T+gkNSqk+0REZpZLruOOOY9q0aTzzzDM89dRTPPzww0ybNo2pU6fy8ssvA3DJJZdw5513ctxxx7F582Z+/etfc/LJJ3POOedw5JFHpvkdKKWUSibtJ1R7en2ulIrn9H5Ca0qpPtGRGNXfDR5U2uMVLg77eofR2NjY5udXX3219fGbb755yP6nn346a9asaf356quv5uqrrz5kv9tuu6318aOP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KCIidUlP33ZhIqm/6CwxJVvYb7/9uOiii9iwYQMABx54oG8TPEOGDKFL5058lbOcg7uUMX1tKi2zWnDggQdGOzSpQ2pqKn379WXRmtlsqEhk4JA94jK5MWzYMG699VaKiopISkpin332iXZIdTrggAOZOHsOX6xJxRH4rJD4FZwKlhCH791YNnTo0GiHIPUUXO67lVZVEhGROvj14nasUVLKBxISEhg7dmy0w9gpZsbIw3/D008/RX5pAj/kpXLUsSNJStKfkt/169efd3+dR2U1HO3zJa6bipkxbNiwaIex0wYPHgzA8wszaZGZQZ8+faIbkESVimmKREZKSmC1Wr3nRESkLkpKhYc/h+OIr+277744B++tSKOsCt8ViZba7bLLLlRUg8P/y8lLQJ8+fUj1To4GDBzo2xGUEhmqWyASGcFpexopJSIitQnOOAlexJDG0fAWqbf+/fuTlJjIxysDq/ANHDgwyhHJzujatWvNtt+K6EvtUlNTefChh8jJyaFfv37RDkeiLC0tbccPEpFGO/HEE9l9990ZMGBAtEMREREfcs4BkJycHOVImgclpaTeUlNTOeHEE/n+u2/p17+/VhSKEaGJqE6dOkUxEqmPXr160atXr2iHIT6QlRUocL777rtHORKR5i0lJYW99tor2mGIiIhP9e3bl7lz52qad5goKSUNcuGFF0Y7BKmnXr16ceedd5KSkqJEokgM6tu3L3fddZdGzYmIiIhE0fnnn8/IkSN1oTBMlJQSiSPBwtkiEnvMTKM3RERERKIsIyODIUOGRDuMZkNVc0VEREREREREJOKUlBIRERERERERkYhTUkpERERERERERCJOSSkREREREREREYk4JaVERERERERERCTilJQSEREREREREZGIU1JKREREREREREQiTkkpERERERERERGJOHPORTsGXzCzXGBptONoIu2BddEOQupNr1vsac6vWQ/nXHa0g4gm9RPiM3rNYlNzft3UT6ifEH/Raxabmuvrtt0+QkmpOGBmM51zw6Idh9SPXrfYo9dMYpX+dmOPXrPYpNdNYpX+dmOPXrPYFI+vm6bviYiIiIiIiIhIxCkpJSIiIiIiIiIiEaekVHyYGO0ApEH0usUevWYSq/S3G3v0msUmvW4Sq/S3G3v0msWmuHvdVFNKREREREREREQiTiOlREREREREREQk4pSUikFm1s3MXjOz+Wa20MzuMrMUMxtsZr8Nedy1ZvbXaMYaz8yssJa2P5nZGXXso9csirb33grTsa8Kx3FEdkR9ROxQPxF71E9Ic6B+Inaon4g96ifqT0mpGGNmBrwMvOqc6wf0B1oA1wODgd9uf+96/67EcB1LApxzDzrnnoh2HLKtHby3GnVcM0sAmmUnIv6iPiL2qZ/wL/UT0hyon4h96if8S/1EwygpFXtGAqXOuckAzrkq4DLgHOBm4BQz+8HMTvEeP8DMPjGzRWZ2cfAgZnaamc3wHvtQsNMws0Izu87Mvgb2i+gziwOhVy7M7GIzm2NmP5nZcyEP28vMPvKy6+d6jzUzu8XMfjazWcHX18wO9V7fKWb2i5k97X0YSv1t7711lpld4F3xeNfM5pnZv4M7mdnl3uvys5ld6rX1NLO5ZnY/8B0wCUj33m9Pb28/kTBQHxHj1E/4mvoJaQ7UT8Q49RO+pn6iAZKiHYDU20Dg29AG59wmM1sCTAb6O+cugsAHFrAbcBiQBcwzsweAvsApwAHOuQrvD/1U4AkgE/jZOfevyDyduHYF0Ms5V2ZmrUPa9wRGEHgtvjeztwh06oOBvYD2wDdm9qn3+CEE/i5WAV8ABwCfR+IJNDPbe28tI/BZORwYBBQT+P9/C3DAH4F9AQO+NrNpwHpgV+CPzrkLAMzsZOfcYG97aG37Oee+b/JnKc2d+ojmRf2Ev6ifkOZA/UTzon7CX9RPNIBGSsUeI/CHu7Ptbznnypxz64AcoCNwODCUwBvhB+92b+/xVcBL4Q5aavUT8LSZnQZUhrS/5pwr8V6zjwl8eB0IPOucq3LOrQWmAft4j5/hnFvhnKsGfgB6RuoJNDM7em994JzLc86VEBiWe6D37xXnXJFzrtBrP8jbb6lz7qvt/K669hNpDPURzYv6CX9RPyHNgfqJ5kX9hL+on2gAJaViz2xgWGiDmbUEuhPoBLZWFrJdRSBDa8DjzrnB3r9dnXPXeo8p9YYZStM7FriPQKf+rZkFRy5u/UHmCLxm21Pbayz1t6P3Vn1fl6I67tOQaGkq6iOaF/UT/qJ+QpoD9RPNi/oJf1E/0QBKSsWeqUCGeSsuePO3bwMeA9YSGFq7M8cYa2YdvGO0NbMeTROu1MYCheq6O+c+Bv4OtCZQBA/geDNLM7N2wKHAN8CnBOb4J5pZNnAwMCPigTdvdb23ioEjvPdKOjCGwNDmT4ExZpZhZpnACcBn2zl+hZkle9v12U+kPtRHNBPqJ3xJ/YQ0B+onmgn1E76kfqIBlJSKMc45R+AP7mQzmw/8CpQSqMT/MYFihKHFCWs7xhzgGuB9M/sJ+ADo3OTBx58MM1sR8u/ykPsSgafMbBbwPXCHc26Dd98M4C3gK+C/zrlVwCsEhuf+CHwE/N05tyZSTyQe7OC9BYF59U8SGNL8knNupnPuOwKdzAzga+CROuZxTwR+MrOn67mfyE5THxFz1E/EEPUT0hyon4g56idiiPqJhrHA/5uIiGyPmZ0JDAsW/hQREQmlfkJEROqifmL7NFJKREREREREREQiTiOlREREREREREQk4jRSSkREREREREREIk5JKRERERERERERiTglpUREREREREREJOKUlBJpImZW5S2p+7OZvWFmrRt4nC5mNiXM4YmISBSpjxARkbqon5B4oULnIk3EzAqdcy287ceBX51z10c5LBER8QH1ESIiUhf1ExIvNFJKJDKmA10BzKyPmb1rZt+a2WdmtltI+1dm9o2ZXWdmhV57TzP72dtOM7PJZjbLzL43s8O89jPN7GXvuPPN7OYoPU8REak/9REiIlIX9RPSbCkpJdLEzCwROBx43WuaCPzZOTcU+Ctwv9d+F3CXc24fYNV2DnchgHNuD+D3wONmlubdNxg4BdgDOMXMuof5qYiISJipjxARkbqon5DmTkkpkaaTbmY/AHlAW+ADM2sB7A+86N33ENDZe/x+wIve9jPbOeaBwJMAzrlfgKVAf+++qc65jc65UmAO0COsz0ZERMJJfYSIiNRF/YTEBSWlRJpOiXNuMIEP9BQCVyYSgA3OucEh/3avxzGtjvvKQrargKT6BiwiIhGjPkJEROqifkLigpJSIk3MObcRuJjA8NoSYLGZnQxgAXt5D/0KOMnbHredw30KnOrt2x/YBZjXRKGLiEgTUx8hIiJ1UT8hzZ2SUiIR4Jz7HviRQAdxKnC2mf0IzAaO9x52KXC5mc0gMAx3Yy2Huh9INLNZwPPAmc65sloeJyIiMUJ9hIiI1EX9hDRn5pyLdgwiAphZBoFhus7MxgG/d84dv6P9RESk+VMfISIidVE/IbFK80RF/GMocK+ZGbABOCu64YiIiI+ojxARkbqon5CYpJFSIiIiIiIiIiIScaopJSIiIiIiIiIiEaeklIiIiIiIiIiIRJySUiIiIiIiIiIiEnFKSomIiIiIiIiISMQpKSUiIiIiIiIiIhGnpJSIiIiIiIiIiEScklIiIiIiIiIiIhJxSkqJiIiIiIiIiEjEKSklIiIiIiIiIiIRp6SUiIiIiIiIiIhEnJJSIiIiIiIiIiIScUpKiYiIiIiIiIhIxCkpJSIiIiIiIiIiEaeklIiIiIiIiIiIRJySUiIi4jtmtsTMZpnZD2Y202tra2YfmNl872ebkMdfaWYLzGyemR0V0j7UO84CM7vbzMxrTzWz5732r82sZ8SfpIiIiIhInFNSSkRE/Oow59xg59ww7/YVwFTnXD9gqncbMxsAjAMGAkcD95tZorfPA8AEoJ/372iv/WxgvXOuL3AHcFMEno+IiIiIiIRQUkpERGLF8cDj3vbjwJiQ9uecc2XOucXAAmC4mXUGWjrnpjvnHPDEVvsEjzUFODw4ikpERERERCJDSSkREfEjB7xvZt+a2QSvraNzbjWA97OD194VWB6y7wqvrau3vXX7Fvs45yqBjUC7JngeIiIiIiKyHUnRDsAv2rdv73r27BntMEREfOnbb79d55zLjuCvPMA5t8rMOgAfmNkvdTy2thFOro72uvbZ8sCBhNgEgMzMzKG77bZb3VGLiMSpKPQTvqPzCRGR2tXVRygp5enZsyczZ86MdhgiIr5kZksj+fucc6u8nzlm9gowHFhrZp2dc6u9qXk53sNXAN1Ddu8GrPLau9XSHrrPCjNLAloB+bXEMRGYCDBs2DCnfkJEpHaR7if8SOcTIiK1q6uP0PQ9ERHxFTPLNLOs4DZwJPAz8Dow3nvYeOA1b/t1YJy3ol4vAgXNZ3hT/ArMbIRXL+qMrfYJHmss8JFXd0pERERERCJEI6VERMRvOgKveHXHk4BnnHPvmtk3wAtmdjawDDgZwDk328xeAOYAlcCFzrkq71jnA48B6cA73j+AScCTZraAwAipcZF4YiIiIiIispmSUiIi4ivOuUXAXrW05wGHb2ef64Hra2mfCQyqpb0UL6klIiIiIiLRoaSUiEiIiooKVqxYQWlpabRDiYq0tDS6detGcnJytEMREfEl9RPqJ0RE6hLP/URD+gglpUREQqxYsYKsrCx69uyJN30sbjjnyMvLY8WKFfTq1Sva4YiI+JL6CfUTIiJ1idd+oqF9hAqdi4iEKC0tpV27dnHVgQSZGe3atYvLqzoiIjtL/YT6CRGRusRrP9HQPkJJKRGRrcRbBxIqnp+7iMjOiufPynh+7iIiOytePysb8ryVlBIRaaQ1a9Ywbtw4+vTpw4ABA/jtb3/LxIkTGTVqVNRiOvTQQ5k5c2bUfr+IiGymfiL8zGyJmc0ysx/MbKbX1tbMPjCz+d7PNiGPv9LMFpjZPDM7KqR9qHecBWZ2t3lnVGaWambPe+1fm1nPiD9JEYkb8dxPKCklItIIzjlOOOEEDj30UBYuXMicOXO44YYbWLt2bViOX11dTUlJSViOJSIiO1ZVVcWcOXNwzoXleE3dT8S5w5xzg51zw7zbVwBTnXP9gKnebcxsADAOGAgcDdxvZonePg8AE4B+3r+jvfazgfXOub7AHcBNEXg+caW0tJT58+dHOwyRqIv3fkJJKRGRRvj4449JTk7mT3/6U03b4MGDOeiggygsLGTs2LHstttunHrqqTUnONdddx377LMPgwYNYsKECTXthx56KP/4xz8YPnw4/fv357PPPiMvL48777yTMWPGcPTRR9OvXz/+/ve/1/yu999/n/3224+9996bk08+mcLCwsj+B4iINDMfffQRF1xwAdOnTw/L8Zq6nwB47LHHOPHEE9VPwPHA497248CYkPbnnHNlzrnFwAJguJl1Blo656a7wH/yE1vtEzzWFOBwi9f5OE3koYce4txzz6WgoCDaoYhEVbz3E0pKiYg0ws8//8zQoUNrve/777/nzjvvZM6cOSxatIgvvvgCgIsuuohvvvmGn3/+mZKSEt58882afSorK5kxYwZ33nkn//nPfyguLgbgxx9/5Pnnn2fWrFk8//zzLF++nHXr1vG///2PDz/8kO+++45hw4Zx++23N/2TFhFpxhYsWADAsmXLwnK8pu4ngn744Yd46ycc8L6ZfWtmE7y2js651QDezw5ee1dgeci+K7y2rt721u1b7OOcqwQ2Au2a4HnErU8//RSAsrKyKEciEl3x3k8kRfS3iYjEkeHDh9OtWzcgcLVjyZIlHHjggXz88cfcfPPNFBcXk5+fz8CBAznuuOMAOPHEEwEYOnQoS5YsqTnWoYceSqtWrQAYMGAAS5cuZcOGDcyZM4cDDjgAgPLycvbbb78IPkMRkeYrXNP36hLOfuLwww+Pt37iAOfcKjPrAHxgZr/U8djaRji5Otrr2mfLAwcSYhMAdtlll7ojllpF4r0mEqvioZ9QUkpEpBEGDhzIlClTar0vNTW1ZjsxMZHKykpKS0u54IILmDlzJt27d+faa6/dYtnU4D7Bx9d1LOccRxxxBM8++2y4n5aISNwL10wt9RNNwzm3yvuZY2avAMOBtWbW2Tm32pual+M9fAXQPWT3bsAqr71bLe2h+6wwsySgFZBfSxwTgYkAw4YNU3alHpSMEgmI935C0/dERBph5MiRlJWV8fDDD9e0ffPNN0ybNq3Wxwc7jPbt21NYWLjdDmhnjBgxgi+++KJmqklxcTG//vprg48nIiKbheuEWf1E+JlZppllBbeBI4GfgdeB8d7DxgOveduvA+O8FfV6EShoPsOb4ldgZiO8elFnbLVP8FhjgY+csihNQv+tEu/ivZ9QUkpEpBHMjFdeeYUPPviAPn36MHDgQK699lq6dOlS6+Nbt27Nueeeyx577MGYMWPYZ599Gvy7s7Ozeeyxx/j973/PnnvuyYgRI/jll7pmL4iIyM4K10gp9RNNoiPwuZn9CMwA3nLOvQvcCBxhZvOBI7zbOOdmAy8Ac4B3gQudc1Xesc4HHiFQ/Hwh8I7XPgloZ2YLgMvxVvKT8Am+x6qrq6MciUh0xXs/YcpMBwwbNszNnDkz2mGISJTNnTuX3XffPdph1Fi6dCmlpaXssssupKenR+R31vZ/YGbfhiy5HZf80E9Mnz6dPffck8zMzKjGIdKcPfDAAzz//PP86U9/Yty4cdvc77d+IhrUT9TOD/1ELDnppJPIy8vjmWee2e7Jt0gsivd+or59hEZKiYiIxICVK1dy5ZVX8sgjj0Q7FJG4oAu3IpFRVVW14weJSLOlpJSIiEgMKC4uBmDWrFlRjkSkeQsmo8I1fU9E6qYEsEh8U1JKREQkhujLu4iINCeqKSUS35SUEhERiSEavSEiIiIizYWSUiIiIjFEI6VEmlYw8av3mkhk6L0mEt+UlBIREYkhGikl0rRUU0okshISdEoqEs/0CSAi4jOJiYkMHjyYQYMGcfbZZ7Np06Y6H//qq68yZ86cHR73wQcf5IknngDgzDPPZMqUKWGJVyJLV5RFJLSfOO6449iwYUOdj1c/ISISX2Kpn0hq9BFERJqxiy7/Gznr8sN2vA7t23Lv7bfU+Zj09HR++OEHAE466SSeeeYZbrjhhu0+/tVXX2XUqFEMGDCgzuP+6U9/qne84j8avSHiL9HuJ8aPH899993H1Vdfvd3Hq58QP9NIKWnu1E/UTUkpEZE65KzLZ2HHQ8J3wLXT6vXwvffem9mzZ+OcY+HChVx44YXk5uaSkZHBww8/TH5+Pq+//jrTpk3jf//7Hy+99BIfffQREydOpLy8nL59+/Lkk0+SkZHBtddeS4sWLfjrX/8avucjEaeRUiL+Eu1+Yr/99uOnn34CUD8hMSXYnykpJc2d+om66RNARMSnqqqq+PLLLxk5ciQAEyZM4J577uHbb7/l1ltv5YILLmD//fdn9OjR3HLLLfzwww/06dOHE088kW+++YYff/yR3XffnUmTJkX5mUg4qM6NSGTEUqHzqqoqpk6dyujRowH1ExJbgu81JaVEmk4s9BMaKSUi4jMlJSUMHjyYJUuWMHDgQPbff38KCwv58ssvOfnkk2seV1ZWVuv+P//8M9dccw0bNmygsLCQo446KlKhi4jEvFhIAIf2E0OHDuWII45QPyExKzExMdohiDQ7sdRPKC0tIuIzwTngS5cupaKigqeffprq6mpat27NDz/8UPNv7ty5te5/5plncu+99zJr1iz+/e9/U1paGuFnICIiTSm0nygvL+e+++5TPyExy88JYJFYFUv9hJJSIiI+1apVK/79738zefJk0tLS6NWrFy+++CIQuJL/448/ApCVlUVBQUHNfgUFBXTu3LkmoSXNQyxNKRKRyGjVqhV33303t956K+np6eonJCYpKSXSdGKhn1BSSkTExwYNGsSuu+7KlClTePrpp5k0aRJ77bUXAwcO5LXXXgNg3Lhx3HLLLQwZMoSFCxfy3//+l3333ZcjjjiC3XbbLcrPQMIlFqYUiUjkDRkyhL322ovnnntO/YTEJF1sEWlafu8nVFNKRKQOHdq3rfcKFzs83g4UFhZucfvBBx+kW7duZGZm8u67727z+AMOOIA5c+bU3D7//PM5//zzt3nctddeW7P92GOP7XzQIiKyXX7oJ954442abfUTEmt0sUWaO/UTdVNSSkSkDvfefku0QwB0FVE205d3kaZV3/eYX/oJERHxJ/UTddP0PRERkRiiBKVIZOi9JhIZeq+JxDclpURERGKARkiJRIbqt4lElt5rIvFNSSkREfElM0s0s+/N7E3vdlsz+8DM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\n",
      "text/plain": [
       "<Figure size 1440x720 with 6 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, axes = plt.subplots(nrows=2,ncols=3)\n",
    "fig.set_size_inches(20, 10)\n",
    "\n",
    "a = sns.violinplot(data = WS, x = \"Region\" , y = \"Fresh\", hue = 'Channel', ax=axes[0][0])\n",
    "b = sns.violinplot(data = WS, x = \"Region\" , y = \"Milk\", hue = 'Channel', ax=axes[0][1])\n",
    "c = sns.violinplot(data = WS, x = \"Region\" , y = \"Grocery\", hue = 'Channel', ax=axes[0][2])\n",
    "d = sns.violinplot(data = WS, x = \"Region\" , y = \"Frozen\", hue = 'Channel',ax=axes[1][0])\n",
    "e = sns.violinplot(data = WS, x = \"Region\" , y = \"Detergents_Paper\", hue = 'Channel',ax=axes[1][1])\n",
    "f = sns.violinplot(data = WS, x = \"Region\" , y = \"Delicatessen\", hue = 'Channel',ax=axes[1][2])\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1.2\n",
    "# Distribution of Varieties across Regions and Channels\n",
    "\n",
    "* Fresh: We know that this variety has the highest contibution across all regions with an Avg of 12000 euros spent. We can see that Hotels spend more on fresh produce as compared to retail stores.\n",
    "\n",
    "* Milk:  We can see that Retail clients spend more on Milk as compared to hotels across all regions.\n",
    "\n",
    "* Grocery: We can see that Retail clients spend more on the variety Grocery as compared to Hotel clients  across all regions.\n",
    "\n",
    "* Frozen:  We can see from the plots above that Hotel clients spend more on Frozen goods as compared to retail stores across all regions.\n",
    "\n",
    "* Detergents_Paper: We can see that Retail clients spend more on Detergetns_Paper as compared to hotels across all regions.\n",
    "\n",
    "* Delicatessen: We know that this variety contibutes to the lowest spending across all regions with an Avg of 1525 euros spent. We can see that the spending is uniform between the channels as compared to the other variables.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1.3 On the basis of the descriptive measure of variability, which item shows the most inconsistent behaviour? Which items shows the least inconsistent behaviour?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "      <th>range</th>\n",
       "      <th>iqr</th>\n",
       "      <th>cov</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Fresh</th>\n",
       "      <td>440.0</td>\n",
       "      <td>12000.297727</td>\n",
       "      <td>12647.328865</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3127.75</td>\n",
       "      <td>8504.0</td>\n",
       "      <td>16933.75</td>\n",
       "      <td>112151.0</td>\n",
       "      <td>112148.0</td>\n",
       "      <td>13806.00</td>\n",
       "      <td>1.053918</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Milk</th>\n",
       "      <td>440.0</td>\n",
       "      <td>5796.265909</td>\n",
       "      <td>7380.377175</td>\n",
       "      <td>55.0</td>\n",
       "      <td>1533.00</td>\n",
       "      <td>3627.0</td>\n",
       "      <td>7190.25</td>\n",
       "      <td>73498.0</td>\n",
       "      <td>73443.0</td>\n",
       "      <td>5657.25</td>\n",
       "      <td>1.273299</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Grocery</th>\n",
       "      <td>440.0</td>\n",
       "      <td>7951.277273</td>\n",
       "      <td>9503.162829</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2153.00</td>\n",
       "      <td>4755.5</td>\n",
       "      <td>10655.75</td>\n",
       "      <td>92780.0</td>\n",
       "      <td>92777.0</td>\n",
       "      <td>8502.75</td>\n",
       "      <td>1.195174</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Frozen</th>\n",
       "      <td>440.0</td>\n",
       "      <td>3071.931818</td>\n",
       "      <td>4854.673333</td>\n",
       "      <td>25.0</td>\n",
       "      <td>742.25</td>\n",
       "      <td>1526.0</td>\n",
       "      <td>3554.25</td>\n",
       "      <td>60869.0</td>\n",
       "      <td>60844.0</td>\n",
       "      <td>2812.00</td>\n",
       "      <td>1.580332</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Detergents_Paper</th>\n",
       "      <td>440.0</td>\n",
       "      <td>2881.493182</td>\n",
       "      <td>4767.854448</td>\n",
       "      <td>3.0</td>\n",
       "      <td>256.75</td>\n",
       "      <td>816.5</td>\n",
       "      <td>3922.00</td>\n",
       "      <td>40827.0</td>\n",
       "      <td>40824.0</td>\n",
       "      <td>3665.25</td>\n",
       "      <td>1.654647</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Delicatessen</th>\n",
       "      <td>440.0</td>\n",
       "      <td>1524.870455</td>\n",
       "      <td>2820.105937</td>\n",
       "      <td>3.0</td>\n",
       "      <td>408.25</td>\n",
       "      <td>965.5</td>\n",
       "      <td>1820.25</td>\n",
       "      <td>47943.0</td>\n",
       "      <td>47940.0</td>\n",
       "      <td>1412.00</td>\n",
       "      <td>1.849407</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  count          mean           std   min      25%     50%  \\\n",
       "Fresh             440.0  12000.297727  12647.328865   3.0  3127.75  8504.0   \n",
       "Milk              440.0   5796.265909   7380.377175  55.0  1533.00  3627.0   \n",
       "Grocery           440.0   7951.277273   9503.162829   3.0  2153.00  4755.5   \n",
       "Frozen            440.0   3071.931818   4854.673333  25.0   742.25  1526.0   \n",
       "Detergents_Paper  440.0   2881.493182   4767.854448   3.0   256.75   816.5   \n",
       "Delicatessen      440.0   1524.870455   2820.105937   3.0   408.25   965.5   \n",
       "\n",
       "                       75%       max     range       iqr       cov  \n",
       "Fresh             16933.75  112151.0  112148.0  13806.00  1.053918  \n",
       "Milk               7190.25   73498.0   73443.0   5657.25  1.273299  \n",
       "Grocery           10655.75   92780.0   92777.0   8502.75  1.195174  \n",
       "Frozen             3554.25   60869.0   60844.0   2812.00  1.580332  \n",
       "Detergents_Paper   3922.00   40827.0   40824.0   3665.25  1.654647  \n",
       "Delicatessen       1820.25   47943.0   47940.0   1412.00  1.849407  "
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "WS_des = WS_var.describe().T\n",
    "WS_des[\"range\"] = WS_des[\"max\"] - WS_des[\"min\"]\n",
    "WS_des[\"iqr\"] = WS_des[\"75%\"] - WS_des[\"25%\"]\n",
    "WS_des[\"cov\"] = (WS_des[\"std\"] / WS_des[\"mean\"]) \n",
    "WS_des"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# By calculating the Coeffient of Variation (COV) we can see that the Item \"Delicatessen\" displays the most consistent behaviour while the item \"Fresh\" displays the least."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x1080 with 42 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(WS_var)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1.4 Are there any outliers in the data? Back up your answer with a suitable plot/technique with the help of detailed comments."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x720 with 6 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, axes = plt.subplots(nrows=2,ncols=3)\n",
    "fig.set_size_inches(20, 10)\n",
    "\n",
    "a = sns.boxplot(data = WS, x = \"Region\" , y = \"Fresh\", hue = 'Channel', ax=axes[0][0])\n",
    "b = sns.boxplot(data = WS, x = \"Region\" , y = \"Milk\", hue = 'Channel', ax=axes[0][1])\n",
    "c = sns.boxplot(data = WS, x = \"Region\" , y = \"Grocery\", hue = 'Channel', ax=axes[0][2])\n",
    "d = sns.boxplot(data = WS, x = \"Region\" , y = \"Frozen\", hue = 'Channel',ax=axes[1][0])\n",
    "e = sns.boxplot(data = WS, x = \"Region\" , y = \"Detergents_Paper\", hue = 'Channel',ax=axes[1][1])\n",
    "f = sns.boxplot(data = WS, x = \"Region\" , y = \"Delicatessen\", hue = 'Channel',ax=axes[1][2])\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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zeSh+W0di8X260Hs70u1MezjaSUdryupryxs//79c3JD0ss/733vew+Zd8+ePbnlllvm5K33vve9c/ahXbt2zb6/Z8+e7Ny5c84YaGacNH98NMjjfBRyxCBjWKnH6aj0e/UwGr3vvvuyb9++bN68ec706enpnPBIHcYqF3TCw3+f6el/OCSOUTE9PZ2TTz4527dvnx1gzbd///5lTT948GC2bduWRx999JD3Dx48mOuvvz6veMUrZqdt3759dt7+97du3Tqn3WuuuSY33HDDEfdtKYute9jLrgS2z9IWyk2DyEvHI9fM3J6zkN/+7d/OqlWr5kzr//xnziIv5pprrpmTg/bv35/rr78+tdbZ/Wl+u4u9t23btjn5Z6atY9kPF9uvB7G/L9XGsI+nlXS8rqS+Hq1h5ad+rcZF09PTOXDgwIJjmoMHDy64zMzdADMOHDiQUsrsMvPv5pm5yyc5dAzUPz4a5HE+CjlikDGs1ON0VPp92CtlpZTLSyk7Syk777///uMR04rzgQ98ILUeW9I9cODAnLPntdbZNg8cOJCbb775kHX2n2mfeX/m7PmM+a8HYbF1D3vZlWAlbZ+VlpuWyhG11kNO7PR//vOvks33wAMPzGm/1pqbb755zv40v93F3pu5aja/rWOx2H49iP19qTaGfTytpON1JfU1WXn5aTkeeeSRIxrrLHSyun9cs9B4ZbEx0Py7CwZ1nI9CjhhkDCvtOJ0xKv0+7JWyWutbkrwlSdavX7+so+mMM85IkrzhDW+YM33z5s3Zdc9XjjjIo/XoSd+RdWeddkgco2LmTNXTnva0vOc97zmmwmz16tU588wzc++99845m1RrzerVq3PhhRfOmf+CCy7IjTfemAMHDsx5f+3atXMS3dq1a486psUstu5hL7sSrKTtM6jcNIi8dDxyzY/92I/N3r44Xyklq1atmjOI6f/8p6amlizM1q5dmwcffHA2B5VScuGFF6bWOrs/zW93sffOPPPMfO5znzukrWOx2H49iP19qTaGfTytpON1JfU1Ga381K/VuGjz5s2599578/Wvf33ZY53Vq1cfUpiVUmbHNSeddNIh45WHH354wTFQ//hokMf5KOSIQcaw0o7TGaPSb98pGwGbNm3K6tUL18dr1qzJmjVrFpzeb9WqVdmyZUtOOOGEQ5ZbtWpVLr300kPWOTNv//vz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\n",
      "text/plain": [
       "<Figure size 1080x576 with 6 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, axes = plt.subplots(nrows=2,ncols=3)\n",
    "fig.set_size_inches(15, 8)\n",
    "\n",
    "a =  sns.boxplot(WS[\"Fresh\"],ax=axes[0][0])\n",
    "b = sns.boxplot(WS[\"Milk\"],ax=axes[0][1])\n",
    "c = sns.boxplot(WS[\"Grocery\"], ax=axes[0][2])\n",
    "d = sns.boxplot(WS[\"Frozen\"],ax=axes[1][0])\n",
    "e = sns.boxplot(WS[\"Detergents_Paper\"],ax=axes[1][1])\n",
    "f = sns.boxplot(WS[\"Delicatessen\"],ax=axes[1][2])\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Outliers: \n",
    "\n",
    " * From the above boxplots we can clearly see the outliers in the given variables. It is evident that Retail stores in general have the least amount of outliers.  \n",
    " * The outliers indicate that most of there are multiple purchases made that are above the third quartile. This indicates that the mean expenditures does not reflect on the actual sales. \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1.5 : \n",
    "Refer Business Report"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Problem 2 \n",
    "\n",
    "The Student News Service at Clear Mountain State University (CMSU) has decided to gather data about the undergraduate students that attend CMSU. CMSU creates and distributes a survey of 14 questions and receives responses from 62 undergraduates (stored in the Survey data set)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "stu = pd.read_csv(\"Survey-1.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Class</th>\n",
       "      <th>Major</th>\n",
       "      <th>Grad Intention</th>\n",
       "      <th>GPA</th>\n",
       "      <th>Employment</th>\n",
       "      <th>Salary</th>\n",
       "      <th>Social Networking</th>\n",
       "      <th>Satisfaction</th>\n",
       "      <th>Spending</th>\n",
       "      <th>Computer</th>\n",
       "      <th>Text Messages</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Female</td>\n",
       "      <td>20</td>\n",
       "      <td>Junior</td>\n",
       "      <td>Other</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2.9</td>\n",
       "      <td>Full-Time</td>\n",
       "      <td>50.0</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>350</td>\n",
       "      <td>Laptop</td>\n",
       "      <td>200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Male</td>\n",
       "      <td>23</td>\n",
       "      <td>Senior</td>\n",
       "      <td>Management</td>\n",
       "      <td>Yes</td>\n",
       "      <td>3.6</td>\n",
       "      <td>Part-Time</td>\n",
       "      <td>25.0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>360</td>\n",
       "      <td>Laptop</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>Junior</td>\n",
       "      <td>Other</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2.5</td>\n",
       "      <td>Part-Time</td>\n",
       "      <td>45.0</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>600</td>\n",
       "      <td>Laptop</td>\n",
       "      <td>200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Male</td>\n",
       "      <td>21</td>\n",
       "      <td>Junior</td>\n",
       "      <td>CIS</td>\n",
       "      <td>Yes</td>\n",
       "      <td>2.5</td>\n",
       "      <td>Full-Time</td>\n",
       "      <td>40.0</td>\n",
       "      <td>4</td>\n",
       "      <td>6</td>\n",
       "      <td>600</td>\n",
       "      <td>Laptop</td>\n",
       "      <td>250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Male</td>\n",
       "      <td>23</td>\n",
       "      <td>Senior</td>\n",
       "      <td>Other</td>\n",
       "      <td>Undecided</td>\n",
       "      <td>2.8</td>\n",
       "      <td>Unemployed</td>\n",
       "      <td>40.0</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>500</td>\n",
       "      <td>Laptop</td>\n",
       "      <td>100</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   ID  Gender  Age   Class       Major Grad Intention  GPA  Employment  \\\n",
       "0   1  Female   20  Junior       Other            Yes  2.9   Full-Time   \n",
       "1   2    Male   23  Senior  Management            Yes  3.6   Part-Time   \n",
       "2   3    Male   21  Junior       Other            Yes  2.5   Part-Time   \n",
       "3   4    Male   21  Junior         CIS            Yes  2.5   Full-Time   \n",
       "4   5    Male   23  Senior       Other      Undecided  2.8  Unemployed   \n",
       "\n",
       "   Salary  Social Networking  Satisfaction  Spending Computer  Text Messages  \n",
       "0    50.0                  1             3       350   Laptop            200  \n",
       "1    25.0                  1             4       360   Laptop             50  \n",
       "2    45.0                  2             4       600   Laptop            200  \n",
       "3    40.0                  4             6       600   Laptop            250  \n",
       "4    40.0                  2             4       500   Laptop            100  "
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stu.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Gender\n",
       "Female    33\n",
       "Male      29\n",
       "dtype: int64"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stu.value_counts(\"Gender\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# For this data, construct the following contingency tables\n",
    "\n",
    "# 2.1 Gender & Major"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>Major</th>\n",
       "      <th>Accounting</th>\n",
       "      <th>CIS</th>\n",
       "      <th>Economics/Finance</th>\n",
       "      <th>International Business</th>\n",
       "      <th>Management</th>\n",
       "      <th>Other</th>\n",
       "      <th>Retailing/Marketing</th>\n",
       "      <th>Undecided</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gender</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Female</th>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>7</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>9</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Male</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>6</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Major   Accounting  CIS  Economics/Finance  International Business  \\\n",
       "Gender                                                               \n",
       "Female           3    3                  7                       4   \n",
       "Male             4    1                  4                       2   \n",
       "\n",
       "Major   Management  Other  Retailing/Marketing  Undecided  \n",
       "Gender                                                     \n",
       "Female           4      3                    9          0  \n",
       "Male             6      4                    5          3  "
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.crosstab(stu['Gender'],stu['Major'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.2 Gender & Grad Intention"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>Grad Intention</th>\n",
       "      <th>No</th>\n",
       "      <th>Undecided</th>\n",
       "      <th>Yes</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gender</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Female</th>\n",
       "      <td>9</td>\n",
       "      <td>13</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Male</th>\n",
       "      <td>3</td>\n",
       "      <td>9</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Grad Intention  No  Undecided  Yes\n",
       "Gender                            \n",
       "Female           9         13   11\n",
       "Male             3          9   17"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.crosstab(stu['Gender'],stu['Grad Intention'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.3 Gender & Employment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>Employment</th>\n",
       "      <th>Full-Time</th>\n",
       "      <th>Part-Time</th>\n",
       "      <th>Unemployed</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gender</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Female</th>\n",
       "      <td>3</td>\n",
       "      <td>24</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Male</th>\n",
       "      <td>7</td>\n",
       "      <td>19</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Employment  Full-Time  Part-Time  Unemployed\n",
       "Gender                                      \n",
       "Female              3         24           6\n",
       "Male                7         19           3"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.crosstab(stu['Gender'],stu['Employment'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.4 Gender & Computer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>Computer</th>\n",
       "      <th>Desktop</th>\n",
       "      <th>Laptop</th>\n",
       "      <th>Tablet</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gender</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Female</th>\n",
       "      <td>2</td>\n",
       "      <td>29</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Male</th>\n",
       "      <td>3</td>\n",
       "      <td>26</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Computer  Desktop  Laptop  Tablet\n",
       "Gender                           \n",
       "Female          2      29       2\n",
       "Male            3      26       0"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.crosstab(stu['Gender'],stu['Computer'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.2.1 What is the probability that a randomly selected CMSU student will be male?\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The probability that a randomly selected student will be male is: 46.77 %\n"
     ]
    }
   ],
   "source": [
    "prob_m = 29/62\n",
    "\n",
    "print(\"The probability that a randomly selected student will be male is:\",round((prob_m)*100,2),\"%\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.2.2  What is the probability that a randomly selected CMSU student will be female?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The probability  that a randomly selected student will be female is: 53.23 %\n"
     ]
    }
   ],
   "source": [
    "prob_f = 33/62\n",
    "\n",
    "print(\"The probability  that a randomly selected student will be female is:\",round((prob_f)*100,2),\"%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.3.1Find the conditional probability of different majors among the male students in CMSU."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The conditional probability among male students based on their majors are :\n",
      "Accounting: 13.79 %\n",
      "CIS: 3.45 %\n",
      "Economics/Finance: 13.79 %\n",
      "International Business: 6.9 %\n",
      "Management: 20.69 %\n",
      "Other: 13.79 %\n",
      "Retailing/Marketing: 17.24 %\n",
      "Undecided: 10.34 %\n"
     ]
    }
   ],
   "source": [
    "#Conditional Prob: \n",
    "#total #male = 29, #female= 33\n",
    "\n",
    "male_acc = (4/29) \n",
    "male_CIS = (1/29) \n",
    "male_Economics_Finance = (4/29) \n",
    "male_International_Business = (2/29)\n",
    "male_Management = (6/29)\n",
    "male_Other = (4/29) \n",
    "male_Retailing_Marketing = (5/29)\n",
    "male_Undecided = (3/29)\n",
    "\n",
    "print(\"The conditional probability among male students based on their majors are :\" )\n",
    "print(\"Accounting:\",round(male_acc*100,2),\"%\")\n",
    "print(\"CIS:\",round(male_CIS*100,2),\"%\")\n",
    "print(\"Economics/Finance:\",round(male_Economics_Finance*100,2),\"%\")\n",
    "print(\"International Business:\",round(male_International_Business*100,2),\"%\")\n",
    "print(\"Management:\",round(male_Management*100,2),\"%\")\n",
    "print(\"Other:\",round(male_Other*100,2),\"%\")\n",
    "print(\"Retailing/Marketing:\",round(male_Retailing_Marketing*100,2),\"%\")\n",
    "print(\"Undecided:\",round(male_Undecided*100,2),\"%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.3.2 Find the conditional probability of different majors among the female students of CMSU."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The conditional probability among female students based on their majors are :\n",
      "Accounting: 9.09 %\n",
      "CIS: 9.09 %\n",
      "Economics/Finance: 21.21 %\n",
      "International Business: 12.12 %\n",
      "Management: 12.12 %\n",
      "Other: 9.09 %\n",
      "Retailing/Marketing: 27.27 %\n",
      "Undecided: 0.0 %\n"
     ]
    }
   ],
   "source": [
    "female_acc = (3/33) \n",
    "female_CIS = (3/33) \n",
    "female_Economics_Finance = (7/33) \n",
    "female_International_Business = (4/33)\n",
    "female_Management = (4/33)\n",
    "female_Other = (3/33) \n",
    "female_Retailing_Marketing = (9/33)\n",
    "female_Undecided = (0/33)\n",
    "\n",
    "\n",
    "print(\"The conditional probability among female students based on their majors are :\")\n",
    "print(\"Accounting:\",round(female_acc*100,2),\"%\")\n",
    "print(\"CIS:\",round(female_CIS*100,2),\"%\")\n",
    "print(\"Economics/Finance:\",round(female_Economics_Finance*100,2),\"%\")\n",
    "print(\"International Business:\",round(female_International_Business*100,2),\"%\")\n",
    "print(\"Management:\",round(female_Management*100,2),\"%\")\n",
    "print(\"Other:\",round(female_Other*100,2),\"%\")\n",
    "print(\"Retailing/Marketing:\",round(female_Retailing_Marketing*100,2),\"%\")\n",
    "print(\"Undecided:\",round(female_Undecided*100,2),\"%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.4.1 Find the probability That a randomly chosen student is a male and intends to graduate."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The probability that a randomly selected student is a male who intends to graduate is : 28.4 %\n"
     ]
    }
   ],
   "source": [
    "#Prob of male graduating\n",
    "#total #males = 29 , females = 33\n",
    "#number of students with the intention of graduating = 11+17 = 28\n",
    "\n",
    "prob_m = 29/62\n",
    "prob_of_grad = 28/62\n",
    "prob_male_grad = 17/28\n",
    "\n",
    "prob_male_and_grad = (prob_m * prob_male_grad) * 100\n",
    "\n",
    "print(\"The probability that a randomly selected student is a male who intends to graduate is :\", round(prob_male_and_grad,1),\"%\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.4.2 Find the probability that a randomly selected student is a female and does NOT have a laptop."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The probability that a randomly selected student is a female and does not have a laptop is: 6.45 %\n"
     ]
    }
   ],
   "source": [
    "#Females with no laptops\n",
    "#total students with no laptops = 7\n",
    "\n",
    "prob_f = 33/62\n",
    "female_no_laptops = 4/33\n",
    "prob_f_and_no_laptop = (prob_f * female_no_laptops) * 100\n",
    "\n",
    "print(\"The probability that a randomly selected student is a female and does not have a laptop is:\", round((prob_f_and_no_laptop),2),\"%\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.5.1 Find the probability that a randomly chosen student is a male or has a full-time employment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The probability that a randomly chosen student is male or has a full time job is: 38.77 %\n"
     ]
    }
   ],
   "source": [
    "prob_m = 29/62\n",
    "prob_full_time = 10/62\n",
    "prob_m_full_time = 7/29\n",
    "\n",
    "prob_m_or_full_time = (prob_m + prob_full_time - prob_m_full_time)*100\n",
    "print(\"The probability that a randomly chosen student is male or has a full time job is:\", round((prob_m_or_full_time),2),\"%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.5.2 Find the conditional probability that given a female student is randomly chosen, she is majoring in international business or management."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The conditional probability that the randomly chosen female student is majoring in International Business or Management is:  48.48 %\n"
     ]
    }
   ],
   "source": [
    "#Cond prob that given a female, she majors in Intl Business or Management\n",
    "#total no of female students = 33\n",
    "#total no of female students in Intl Business = 4 , Management = 4\n",
    "\n",
    "prob_f_majors = 1/33\n",
    "female_International_Business = 4/33 \n",
    "female_Management = 4/33\n",
    "prob_female_Intl_or_Manage = (female_International_Business * female_Management)\n",
    "prob_f_majors_Int_or_Manage = (prob_female_Intl_or_Manage/prob_f_majors) * 100\n",
    "\n",
    "print(\"The conditional probability that the randomly chosen female student is majoring in International Business or Management is: \",round((prob_f_majors_Int_or_Manage),2),\"%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.6 Construct a contingency table of Gender and Intent to Graduate at 2 levels (Yes/No). The Undecided students are not considered now and the table is a 2x2 table. Do you think graduate intention and being female are independent events?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "noun_stu = pd.crosstab(stu['Gender'],stu['Grad Intention'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>Grad Intention</th>\n",
       "      <th>No</th>\n",
       "      <th>Yes</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gender</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Female</th>\n",
       "      <td>9</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Male</th>\n",
       "      <td>3</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Grad Intention  No  Yes\n",
       "Gender                 \n",
       "Female           9   11\n",
       "Male             3   17"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "noun_stu.drop('Undecided', axis =1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# The two events are independent because a randomly selected student can be a female and can have of either have the intention to graduate or not."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.7 Note that there are four numerical (continuous) variables in the data set, GPA, Salary, Spending and Text Messages. Answer the following questions based on the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Class</th>\n",
       "      <th>Major</th>\n",
       "      <th>Grad Intention</th>\n",
       "      <th>GPA</th>\n",
       "      <th>Employment</th>\n",
       "      <th>Salary</th>\n",
       "      <th>Social Networking</th>\n",
       "      <th>Satisfaction</th>\n",
       "      <th>Spending</th>\n",
       "      <th>Computer</th>\n",
       "      <th>Text Messages</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>57</th>\n",
       "      <td>58</td>\n",
       "      <td>Female</td>\n",
       "      <td>21</td>\n",
       "      <td>Senior</td>\n",
       "      <td>International Business</td>\n",
       "      <td>No</td>\n",
       "      <td>2.4</td>\n",
       "      <td>Part-Time</td>\n",
       "      <td>40.0</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1000</td>\n",
       "      <td>Laptop</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>58</th>\n",
       "      <td>59</td>\n",
       "      <td>Female</td>\n",
       "      <td>20</td>\n",
       "      <td>Junior</td>\n",
       "      <td>CIS</td>\n",
       "      <td>No</td>\n",
       "      <td>2.9</td>\n",
       "      <td>Part-Time</td>\n",
       "      <td>40.0</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>350</td>\n",
       "      <td>Laptop</td>\n",
       "      <td>250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>59</th>\n",
       "      <td>60</td>\n",
       "      <td>Female</td>\n",
       "      <td>20</td>\n",
       "      <td>Sophomore</td>\n",
       "      <td>CIS</td>\n",
       "      <td>No</td>\n",
       "      <td>2.5</td>\n",
       "      <td>Part-Time</td>\n",
       "      <td>55.0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>500</td>\n",
       "      <td>Laptop</td>\n",
       "      <td>500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>60</th>\n",
       "      <td>61</td>\n",
       "      <td>Female</td>\n",
       "      <td>23</td>\n",
       "      <td>Senior</td>\n",
       "      <td>Accounting</td>\n",
       "      <td>Yes</td>\n",
       "      <td>3.5</td>\n",
       "      <td>Part-Time</td>\n",
       "      <td>30.0</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>490</td>\n",
       "      <td>Laptop</td>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>61</th>\n",
       "      <td>62</td>\n",
       "      <td>Female</td>\n",
       "      <td>23</td>\n",
       "      <td>Senior</td>\n",
       "      <td>Economics/Finance</td>\n",
       "      <td>No</td>\n",
       "      <td>3.2</td>\n",
       "      <td>Part-Time</td>\n",
       "      <td>70.0</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>250</td>\n",
       "      <td>Laptop</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    ID  Gender  Age      Class                   Major Grad Intention  GPA  \\\n",
       "57  58  Female   21     Senior  International Business             No  2.4   \n",
       "58  59  Female   20     Junior                     CIS             No  2.9   \n",
       "59  60  Female   20  Sophomore                     CIS             No  2.5   \n",
       "60  61  Female   23     Senior              Accounting            Yes  3.5   \n",
       "61  62  Female   23     Senior       Economics/Finance             No  3.2   \n",
       "\n",
       "   Employment  Salary  Social Networking  Satisfaction  Spending Computer  \\\n",
       "57  Part-Time    40.0                  1             3      1000   Laptop   \n",
       "58  Part-Time    40.0                  2             4       350   Laptop   \n",
       "59  Part-Time    55.0                  1             4       500   Laptop   \n",
       "60  Part-Time    30.0                  2             3       490   Laptop   \n",
       "61  Part-Time    70.0                  2             3       250   Laptop   \n",
       "\n",
       "    Text Messages  \n",
       "57             10  \n",
       "58            250  \n",
       "59            500  \n",
       "60             50  \n",
       "61              0  "
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stu.tail() # [\"GPA\",\"Salary\",\"Spending\",\"Text Messages\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.7.1 If a student is chosen randomly, what is the probability that his/her GPA is less than 3?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>GPA</th>\n",
       "      <th>2.3</th>\n",
       "      <th>2.4</th>\n",
       "      <th>2.5</th>\n",
       "      <th>2.6</th>\n",
       "      <th>2.8</th>\n",
       "      <th>2.9</th>\n",
       "      <th>3.0</th>\n",
       "      <th>3.1</th>\n",
       "      <th>3.2</th>\n",
       "      <th>3.3</th>\n",
       "      <th>3.4</th>\n",
       "      <th>3.5</th>\n",
       "      <th>3.6</th>\n",
       "      <th>3.7</th>\n",
       "      <th>3.8</th>\n",
       "      <th>3.9</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gender</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Female</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Male</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "GPA     2.3  2.4  2.5  2.6  2.8  2.9  3.0  3.1  3.2  3.3  3.4  3.5  3.6  3.7  \\\n",
       "Gender                                                                         \n",
       "Female    1    1    2    0    1    3    5    2    4    3    2    4    1    2   \n",
       "Male      0    0    4    2    2    1    2    5    2    2    5    2    2    0   \n",
       "\n",
       "GPA     3.8  3.9  \n",
       "Gender            \n",
       "Female    1    1  \n",
       "Male      0    0  "
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.crosstab(stu['Gender'],stu['GPA'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The probability of the student's GPA being less than 3 is:  27.42 %\n"
     ]
    }
   ],
   "source": [
    "#no of students with GPA < 3 = 8+9 = 17\n",
    "#total no of students = 62\n",
    "\n",
    "prob_GPA_less_than_three = (17/62)*100\n",
    "print(\"The probability of the student's GPA being less than 3 is: \",round((prob_GPA_less_than_three),2),\"%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.7.2 Find conditional probability that a randomly selected male earns 50 or more. Find conditional probability that a randomly selected female earns 50 or more."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>Salary</th>\n",
       "      <th>25.0</th>\n",
       "      <th>30.0</th>\n",
       "      <th>35.0</th>\n",
       "      <th>37.0</th>\n",
       "      <th>37.5</th>\n",
       "      <th>40.0</th>\n",
       "      <th>42.0</th>\n",
       "      <th>45.0</th>\n",
       "      <th>47.0</th>\n",
       "      <th>47.5</th>\n",
       "      <th>50.0</th>\n",
       "      <th>52.0</th>\n",
       "      <th>54.0</th>\n",
       "      <th>55.0</th>\n",
       "      <th>60.0</th>\n",
       "      <th>65.0</th>\n",
       "      <th>70.0</th>\n",
       "      <th>78.0</th>\n",
       "      <th>80.0</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gender</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Female</th>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Male</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Salary  25.0  30.0  35.0  37.0  37.5  40.0  42.0  45.0  47.0  47.5  50.0  \\\n",
       "Gender                                                                     \n",
       "Female     0     5     1     0     1     5     1     1     0     1     5   \n",
       "Male       1     0     1     1     0     7     0     4     1     0     4   \n",
       "\n",
       "Salary  52.0  54.0  55.0  60.0  65.0  70.0  78.0  80.0  \n",
       "Gender                                                  \n",
       "Female     0     0     5     5     0     1     1     1  \n",
       "Male       1     1     3     3     1     0     0     1  "
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.crosstab(stu['Gender'],stu['Salary'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The conditional probability that a selected male earns 50 or more is: 43.75 %\n",
      "The conditional probability that a selected female earns 50 or more is: 56.25 %\n"
     ]
    }
   ],
   "source": [
    "#total no of students = 62 ; male = 29 female = 33\n",
    "#total no of students with salary >= 50 : male = 14 + female = 18 ; total = 32\n",
    "\n",
    "prob_m_50plus = (14/32)*100\n",
    "prob_f_50plus = (18/32)*100\n",
    "\n",
    "print(\"The conditional probability that a selected male earns 50 or more is:\",round((prob_m_50plus),2),\"%\")\n",
    "print(\"The conditional probability that a selected female earns 50 or more is:\",round((prob_f_50plus),2),\"%\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.8.1 Note that there are four numerical (continuous) variables in the data set, GPA, Salary, Spending and Text Messages. For each of them comment whether they follow a normal distribution."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "new_stu = stu.drop([\"ID\",\"Age\",\"Social Networking\",\"Satisfaction\"], axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>GPA</th>\n",
       "      <td>62.0</td>\n",
       "      <td>3.129032</td>\n",
       "      <td>0.377388</td>\n",
       "      <td>2.3</td>\n",
       "      <td>2.9</td>\n",
       "      <td>3.15</td>\n",
       "      <td>3.4</td>\n",
       "      <td>3.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Salary</th>\n",
       "      <td>62.0</td>\n",
       "      <td>48.548387</td>\n",
       "      <td>12.080912</td>\n",
       "      <td>25.0</td>\n",
       "      <td>40.0</td>\n",
       "      <td>50.00</td>\n",
       "      <td>55.0</td>\n",
       "      <td>80.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Spending</th>\n",
       "      <td>62.0</td>\n",
       "      <td>482.016129</td>\n",
       "      <td>221.953805</td>\n",
       "      <td>100.0</td>\n",
       "      <td>312.5</td>\n",
       "      <td>500.00</td>\n",
       "      <td>600.0</td>\n",
       "      <td>1400.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Text Messages</th>\n",
       "      <td>62.0</td>\n",
       "      <td>246.209677</td>\n",
       "      <td>214.465950</td>\n",
       "      <td>0.0</td>\n",
       "      <td>100.0</td>\n",
       "      <td>200.00</td>\n",
       "      <td>300.0</td>\n",
       "      <td>900.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               count        mean         std    min    25%     50%    75%  \\\n",
       "GPA             62.0    3.129032    0.377388    2.3    2.9    3.15    3.4   \n",
       "Salary          62.0   48.548387   12.080912   25.0   40.0   50.00   55.0   \n",
       "Spending        62.0  482.016129  221.953805  100.0  312.5  500.00  600.0   \n",
       "Text Messages   62.0  246.209677  214.465950    0.0  100.0  200.00  300.0   \n",
       "\n",
       "                  max  \n",
       "GPA               3.9  \n",
       "Salary           80.0  \n",
       "Spending       1400.0  \n",
       "Text Messages   900.0  "
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_stu.describe().T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAWAAAAFgCAYAAACFYaNMAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAAAvNElEQVR4nO3deXhV9b3v8fc380QSCCFASJgEBFFAEXHCAUUcqrbaqh201ha1tbXH3nvac3rac3rv7T3tOa3tU22r2FptT492cK6I4ATiCCjzPBMCSZiSABlI8r1/ZNubpgECZO/fTvbn9Tzryd5rrb33B1h8WKy91m+ZuyMiIrGXFDqAiEiiUgGLiASiAhYRCUQFLCISiApYRCSQlNAButL06dN99uzZoWOIiLRnHc3sUXvAu3fvDh1BRKTTelQBi4h0JypgEZFAVMAiIoGogEVEAlEBi4gEogIWEQlEBSwiEogKWEQkEBWwiEggKmARkUCiVsBmVmJmr5vZajNbaWb3Rub3MbO5ZrY+8rP3EV4/3czWmtkGM/tWtHKKiIQSzT3gJuAb7j4amAx8xczGAN8CXnX3EcCrked/w8ySgZ8DVwJjgFsirxUR6TGiVsDuvtPdP4g8rgVWA8XAdcDjkdUeB67v4OWTgA3uvsndG4EnI68TEekxYnIM2MyGABOA94Aid98JrSUN9OvgJcXA9jbPyyLzOnrvGWa2yMwWVVVVdWlu6V5KSgdjZnE3lZQODv1bI3Eq6uMBm1kO8BTwdXevMetwWMy/e1kH8zq8fbO7zwRmAkycOFG3eE5gZdu3cf+ctaFj/J37po0KHUHiVFT3gM0sldby/b27Px2ZXWFmAyLLBwCVHby0DChp83wQUB7NrCIisRbNsyAM+DWw2t3vb7PoeeC2yOPbgOc6ePlCYISZDTWzNODmyOtERHqMaO4Bnw98DrjUzJZEpquAHwCXm9l64PLIc8xsoJnNAnD3JuAe4GVav7z7o7uvjGJWEZGYi9oxYHdfwBHugwRM7WD9cuCqNs9nAbOik05EJDxdCSciEogKWEQkEBWwiEggKmARkUBUwCIigaiARUQCUQGLiASiAhYRCUQFLCISiApYRCQQFbCISCAqYBGRQFTAIiKBqIBFRAJRAYuIBKICFhEJRAUsIhKIClhEJBAVsIhIICpgEZFAVMAiIoGogEVEAlEBi4gEogIWEQlEBSwiEogKWEQkEBWwiEggKdF6YzN7FLgGqHT3sZF5fwBGRVbJB/a7+/gOXrsFqAWagSZ3nxitnCIioUStgIHHgAeB3340w91v+uixmf0YqD7K6y9x991RSyciEljUCtjd55vZkI6WmZkBnwIujdbni4jEu1DHgC8EKtx9/RGWOzDHzBab2YwY5hIRiZloHoI4mluAJ46y/Hx3LzezfsBcM1vj7vM7WjFS0DMASktLuz6piEiUxHwP2MxSgE8AfzjSOu5eHvlZCTwDTDrKujPdfaK7TywsLOzquCIiURPiEMRlwBp3L+tooZllm1mvjx4D04AVMcwnIhITUStgM3sCeAcYZWZlZnZHZNHNtDv8YGYDzWxW5GkRsMDMlgLvAy+6++xo5RQRCSWaZ0HccoT5n+9gXjlwVeTxJmBctHKJiMQLXQknIhKIClhEJBAVsIhIICpgEZFAVMAiIoGogEVEAlEBi4gEogIWEQlEBSwiEogKWEQkEBWwiEggKmARkUBUwCIigaiARUQCUQGLiASiAhYRCUQFLCISiApYRCQQFbCISCAqYBGRQFTAIiKBqIBFRAJRAYuIBKICFhEJRAUsIhKIClhEJBAVsIhIICpgEZFAolbAZvaomVWa2Yo28/7NzHaY2ZLIdNURXjvdzNaa2QYz+1a0MoqIhBTNPeDHgOkdzP+Ju4+PTLPaLzSzZODnwJXAGOAWMxsTxZwiIkFErYDdfT6w9wReOgnY4O6b3L0ReBK4rkvDiYjEgRDHgO8xs2WRQxS9O1heDGxv87wsMq9DZjbDzBaZ2aKqqqquzioiEjWxLuBfAsOB8cBO4McdrGMdzPMjvaG7z3T3ie4+sbCwsEtCiojEQkwL2N0r3L3Z3VuAR2g93NBeGVDS5vkgoDwW+UREYimmBWxmA9o8/TiwooPVFgIjzGyomaUBNwPPxyKfiEgspUTrjc3sCeBioK+ZlQH/ClxsZuNpPaSwBbgzsu5A4FfufpW7N5nZPcDLQDLwqLuvjFZOEZFQolbA7n5LB7N/fYR1y4Gr2jyfBfzdKWoiIj2JroQTEQlEBSwiEogKWEQkEBWwiEggKmARkUBUwCIigaiARUQCUQGLiASiAhYRCUQFLCISiApYRCSQqI0FIdJTtbhTUVNPZW0Dew80sq+ukYbDLTQ0tdDU3EJykpGSlERGWhK9MlLJn3Irzy3ZwdjiPIYWZJOU1NGQ15KIVMAindDc4mzefZD1FbVs3XuIhqYWANKSk+idnUpWWjK9s9NISTKaW5ymFqeusZmd++vInfQJ7n1yCQC90lM4Z1gBF5xSwMWj+jGkb3bAX5WEpgIWOYr6w80s2b6fFeXVHGxoJistmWGF2QwpyGZAXgY56SmYHX2P9r7pY1i5fS8ry6v5YNt+3tqwm1dWV8ALqzhtYC5XnzGA68cXMzA/M0a/KokXKmCRDjQ1t7C0rJqFW/bS0NTC4IIsLh2Vx5C+2SQdo3D/TkszYwbmMmZgLp+c2Hqzl217DjFn1S5eXL6T/5i9lh+9vJZLT+3HZ84ZzEUjC3WYIkGogEXa2bG/jrmrKqiuO8zggiwuOKUvfXPSu/QzSguy+OKFw/jihcPYtucQTy7cxh8XlfHK6oWMLMrhrouG87FxA0lN1vfkPZn+dEUimluctzbs5s+LywD4+IRirh9f3OXl215pQRb/OP1U3v7WpfzkpnEA3PfHpVx2/zz+sqwc9yPek1a6Oe0BiwCHGpt4YelOdtXUc9rAXKaMKCQtJbb7J2kpSXx8wiCuG1fMK6sruH/uOu757w95pGQz371mDGcN7h3TPBJ92gOWhLfnQAN/WLid3QcauGpsfy4bXRTz8m0rKcmYdlp/XvzahfznjWdQUV3PDb98m28/s5zqusPBcknXUwFLQtuxv44/Li6jqcW54axBjCjqFTrSXyUnGZ+cWMKr37iIOy4YyhPvb+Oy++fx2pqK0NGki6iAJWGV76/juSU7yE5L5qaJJfTPzQgdqUPZ6Sl855oxPH/PBRRkp/GFxxbxr8+toP5wc+hocpJUwJKQdlXX89yScrLTU7jhzEHkZqaGjnRMY4vzePYr53PHBUN5/J2tXPfgW2zdczB0LDkJKmBJOHsONPDMkh1kpiVzw4RBZKd3n++iM1KT+c41Y3js9rOpqK3n2gff4s31VaFjyQlSAUtCOdTYxPNLy0lJMj5xZjE5Gd2nfNu6eFQ/nv/KBQzIy+C2R9/nN29tDh1JToAKWBJGU3MLf1m2k0ONzXxs3EByM+L/sMPRlBZk8fSXz+PyMUV874VV/HD2Gp0z3M2ogCUhuDuvrqlkZ3U908YUxe0XbscrKy2FX3zmLD59Tim/fGMj33xqGU3NLaFjSSd1z/9/iRynlTtrWLOrlslD+8TVqWZdITnJ+P71Y+mbk87PXl1PQ1ML939qPMkaTyLuqYClx9t9oIF5a6so6ZPJ2UP7hI4TFWbGfZePJDM1mR/OXkNykvGjG8dpUJ84F7UCNrNHgWuASncfG5n3n8DHgEZgI3C7u+/v4LVbgFqgGWhy94nRyik92+HmFl5avou0lCSuGNP/+Ecy62buvng4h5tbuH/uOlKTkvjBDacfc7hMCSeax4AfA6a3mzcXGOvuZwDrgH86yusvcffxKl85GW+u383eQ41ccVr/bnW62cn42tQRfPXSU/jDou3cP3dd6DhyFFHbIt19vpkNaTdvTpun7wI3RuvzRbbtPcTyHdVMKM2ntE9W6Dgxdd/lI6msaeCB1zZQnJ/JzZNKQ0eSDoQ8C+ILwEtHWObAHDNbbGYzjvYmZjbDzBaZ2aKqKp2QLq0am1p4ZXUF+VmpnDesIHScmDMz/s/HxzJlZCHffnYFb6ytDB1JOhCkgM3s20AT8PsjrHK+u58JXAl8xcymHOm93H2mu09094mFhYVRSCvd0YINu6mtb+Ly0UWkJOig5qnJSfziM2cyqqgXX33iQzbv1mXL8SbmW6aZ3Ubrl3Of8SOcNe7u5ZGflcAzwKTYJZTubse+utZDDyX5CX+ftZz0FGbeehYpScadv1vEwYam0JGkjZgWsJlNB74JXOvuh46wTraZ9froMTANWBG7lNKdNbc4r6+tpFdGCucOT7xDDx0Z1DuLB245kw2VB/jHp5bpark4ErUCNrMngHeAUWZWZmZ3AA8CvYC5ZrbEzB6KrDvQzGZFXloELDCzpcD7wIvuPjtaOaVnWVq2nz0HG5kyolD3U2vjghF9+cfpp/Lisp385q0toeNIRDTPgrilg9m/PsK65cBVkcebgHHRyiU9V3JOH97dtIfBBVkML8wOHSfu3DllGIu27OMHL61h8rACxgzMDR0p4WkXQXqM3pd8gRaHi0cW6uKDDpgZ/3HjGeRnpfK1Jz+krlEDuoeWGGemS4+3eOs+ssdczFmlvcnPSgsd529ZUlz9g5AxeBxFN3+fQdd8law1L7J929bQkRKWCli6PXfn+y+uounAXs4aPDx0nL/nLdw/Z23oFH9jwfrdLOZqKja8FzpKQtMhCOn2Zi3fxQfb9lP95n8FvZtxdzJ5eB/6ZKdRMP0eaut1p+VQtLVKt9bQ1MwPZq/m1P69OLD8ldBxuo2UpCQuH11Eck4B//7SmtBxEpYKWLq1372zle176/jnq0aDayDy49E/L4Oahc/y3+9t4+0Nu0PHSUgqYOm2DjY08Ys3NnLBKX2ZMlKXoZ+I6gW/Z2jfbL719HLd5j4AFbB0W4+9vYW9Bxv5xrSRoaN0W97UyPevH8u2vYf45RsbQ8dJOCpg6Zaq6w7z8LyNTD21HxNKe4eO062dd0pfPjZuIL+ct5GtezRgTyypgKVb+vWCzdTUN/EPl2vvtyv8y9WjSUtO4l+fX6mxImJIBSzdzr6DjTy6YDNXju3P2OK80HF6hKLcDP7h8pG8sbaKl1dWhI6TMDpVwGZ2fmfmicTCw/M3cbBRe79d7bZzBzOqqBf/d9ZqGpr0hVwsdHYP+IFOzhOJqqraBh5/ewvXjhvIyB52e/nQUpKT+PbVo9m29xCPv70ldJyEcNRLkc3sXOA8oNDM7muzKBdIjmYwkY48PG8jjc0t3Dt1ROgoPdKUkYVcMqqQB17dwA1nDqIgJz10pB7tWHvAaUAOrUXdq81Ug26oKTFWfegw//3+Nj52xgCGFeaEjtNjffvq0Rw63MxPX1kfOkqPd9Q9YHefB8wzs8fcXUMmSVC/e3cLhxqbufOiOBxwpwc5pV8vPnNOKb9/bxu3nTeYU/rpUE+0dPYYcLqZzTSzOWb22kdTVJOJtFF/uJnH3t7CxaMKGT1AA4lH271TR5CRksT9c9eFjtKjdXY4yj8BDwG/AvT1qMTcUx+UsftAI3dO0d5vLBTkpHPHBUP52WsbWLGjWqf7RUln94Cb3P2X7v6+uy/+aIpqMpGI5hbnkfmbGDcoj8nD+oSOkzC+OGUYeZmp/CjOxjLuSTpbwC+Y2ZfNbICZ9floimoykYiXV+5iy55D3HXR8Li6s0RPl5uRyt0XD+eNtVW8v3lv6Dg9UmcL+DbgfwJvA4sj06JohRL5iLvz0LyNDCnIYtpp/UPHSTi3nTuEwl7p/OjltbpEOQo6VcDuPrSDaVi0w4m8s2kPy8qq+dKUYSQnae831jLTkvnapafw/pa9zF+vMYO7Wqe+hDOzWzua7+6/7do4In/r4Xmb6JuTxg1nDgodJWHddHYpD8/fxH++vIYpI/rqMFAX6uwhiLPbTBcC/wZcG6VMIgCsKq9h3roqbj9/KBmpuvAylLSUJL5+2UhW7KhhzioN1NOVOnsI4qttpi8BE2i9Sk4kambO30h2WjKfPWdw6CgJ7/rxAxlckMWDr23QseAudKLDUR4CdDG+RE3ZvkO8sGwnt0wqJS8rNXSchJeSnMSXLx7O8h3VzFtXFTpOj9HZ4ShfMLPnI9OLwFrguehGk0T2qzc3Y8AXLhgaOopEfHzCIAbmZfCA9oK7TGf3gH8E/Dgy/V9girt/62gvMLNHzazSzFa0mdfHzOaa2frIzw7vJWNm081srZltMLOjfo70PPsONvKHhdu5bnwxA/MzQ8eRiLSUJO66eDiLt+7j3U06L7grdPYY8DxgDa0jofUGGjvxsseA6e3mfQt41d1HAK9Gnv8NM0sGfg5cCYwBbjGzMZ3JKT3Db9/ZSt3hZmZM0ZmO8eZTE0so7JXOz1/fEDpKj9DZQxCfAt4HPgl8CnjPzI46HKW7zwfa/zN5HfB45PHjwPUdvHQSsMHdN7l7I/Bk5HWSAOoam3n8nS1cemo/RvXXKFzxJiM1mRkXDmPBht18sG1f6DjdXmcPQXwbONvdb3P3W2ktye+cwOcVuftOgMjPfh2sUwxsb/O8LDKvQ2Y2w8wWmdmiqip9OdDd/XnxdvYebOQuDTkZtz59Tim9s1L5+WvaCz5ZnS3gJHevbPN8z3G89nh1dJb3EY/4u/tMd5/o7hMLCwujFElioam5hZlvbmJCaT5nD9Gt5uNVdnoKd1wwlFfXVLKyvDp0nG6tsyU628xeNrPPm9nngReBWSfweRVmNgAg8rOyg3XKgJI2zwcB5SfwWdLNvLRiF9v31nHnFA26E+9uPW8IOekpzJy/KXSUbu2oBWxmp5jZ+e7+P4GHgTOAccA7wMwT+LznaR3Yh8jPjk5lWwiMMLOhZpYG3Bx5nfRg7s7D8zcyrG8208YUhY4jx5Cbkcotk0r4y7KdlO07FDpOt3WsPeCfArUA7v60u9/n7v9A697vT4/2QjN7gtaiHmVmZWZ2B/AD4HIzWw9cHnmOmQ00s1mRz2kC7gFeBlYDf3T3lSf2y5Pu4q0Ne1ixo4YZU4aRpEF3uoXbzx+KAb9esDl0lG7rWIPxDHH3Ze1nuvsiMxtytBe6+y1HWDS1g3XLgavaPJ/FiR3ikG7q4fkbKeyVzvUTjvh9q8SZgfmZXDtuIH9YuJ17p44gP0ujExyvY+0BZxxlmc6Qly6xYkc1b67fzRc06E63M+OiYRxqbOa/3tU9e0/EsQp4oZl9qf3MyOEE3ZJIusTD8zeRk57Cp88pDR1FjtOp/XO5aGQhj729lfrDul3k8TpWAX8duN3M3jCzH0emecAXgXujnk56vO17D/HisnI+c04peZkadKc7unPKMHYfaOCZD3eEjtLtHLWA3b3C3c8DvgdsiUzfc/dz3X1X9ONJT/fIm5tITjJuP1+D7nRX5w4vYGxxLo/M30RLiwbpOR6dHQvidXd/IDK9Fu1Qkhj2HGjgj4u2c/34YvrnHe3rBolnZsaMKcPZtPsgr6zWgO3HI1pXs4kc02/f2Ur94RbuvEiD7nR3V43tT3F+Jo++pVPSjocKWII41NjE4+9s4bLRRZzST4PudHcpyUncdt5g3t20V5cnHwcVsATxx4Xb2X/oMHdp77fHuGliKVlpyTy6YEvoKN2GClhirqm5hUfe3MzEwb2ZOKRP6DjSRfKyUrnxrEG8sLScytr60HG6BRWwxNyLy3eyY38dd2rIyfAsCTPrsunfb7+CxuYWRl55x0m9T0lpYtyI9ViXIot0KXfnl29s5JR+OUw9taPhoCWmvIX756zt0rd8bskOKi75HN/+l++Qknxi+3j3TRvVpZnilfaAJaZeW1PJml213H3RcA2600NNKO1N3eFm1lbUho4S91TAEjPuzi/e2EhxfibXjh8YOo5ESUnvTAqy01iyfb/unnwMKmCJmfc372Xx1n3MmDKM1BP8r6nEPzNjfGk+uw80UravLnScuKa/BRIzv3hjIwXZaXxqYsmxV5Zu7dSiXmSmJrNk+/7QUeKaClhiYsWOauatq+L284eQmaYhJ3u6lOQkTi/OY9Pug+w/1Bg6TtxSAUtMPDRvIznpKXzu3CGho0iMnDEojyRDe8FHoQKWqNuy+yCzlu/kM5M15GQiyU5PYWRRL1btrKFBYwV3SAUsUffz1zeQkpzEHRdoyMlEM74kn8PNzsqdNaGjxCUVsETVlt0HefrDHXzmnFL69dKQk4mmKDeDgfkZLNm+X2MFd0AFLFH1wGsbSEky7tZlxwlrQklvauub2LT7YOgocUcFLFGzefdBnvmwjM9OHky/XO39JqphhdnkZqTw4fZ9oaPEHRWwRM0Dr64nLSWJu7T3m9CSzBhXkk/5/noqazRKWlsqYImKjVUHeHbJDj43eTCFvdJDx5HAThuQS2qy6ZS0dhK+gEtKB3fpcHxdNXX34fh+9up60lOSNeSkAJCemsyYAbmsqzjAwYam0HHiRsIPR1m2fVuXD8fXFbrzcHwbKmt5fmk5M6YMo2+O9n6l1biSfJaWVbN8RzWThxWEjhMXEn4PWLre/XPXkZmazIwLdbsh+f96Z6UxpCCLZWXVNLW0hI4TF1TA0qU+2LaPWct3MWPKMAq09yvtjC/Jp+5wM+sqDoSOEhdiXsBmNsrMlrSZaszs6+3WudjMqtus891Y55Tj5+78+6zV9M1J50va+5UOlPbJoo/GCv6rmB8Ddve1wHgAM0sGdgDPdLDqm+5+TQyjyUmau6qChVv28f2PjyU7PeG/XpAOmBnjS/J5bU0l5fvrKe6dGTpSUKEPQUwFNrr71sA55CQ1Nbfwg9lrGFaYzU0a71eO4tT+vchISdKFGYQv4JuBJ46w7FwzW2pmL5nZaUd6AzObYWaLzGxRVVVVdFLKMf3Xu1vZVHWQb00/9YRvxCiJITU5ibHFeWyqOkhN3eHQcYIK9jfFzNKAa4E/dbD4A2Cwu48DHgCePdL7uPtMd5/o7hMLCwujklWOrqq2gR/PXceFI/py+Zii0HGkGzhjUB4YLC3bHzpKUCF3Va4EPnD3ivYL3L3G3Q9EHs8CUs2sb6wDSuf8x+w11B9u5t+uPQ0z3elYjq1XRioj+uWworyGxqbEPSUtZAHfwhEOP5hZf4v8TTazSbTm3BPDbNJJH2zbx58Wl/GFC4YyvDAndBzpRsaX5NPY1MLqBB4rOEgBm1kWcDnwdJt5d5nZXZGnNwIrzGwp8DPgZtc5K3GnqbmF7z63gqLcdL566YjQcaSbGZCXSf/cjIQ+JS3IuULufggoaDfvoTaPHwQejHUuOT6PvLmZFTtqePDTE8jRaWdyAsaX5DN75S627DnE0L7ZoePEnL6ulhOyofIAP3llHdNP68/Vpw8IHUe6qVP65ZCdnri3r1cBy3ErGTyEC77xEHW11Txy92UkJSUFHz1OX/51T8lJxhmD8tm29xB7DjSEjhNz+n+jHLfqogn0KR7NtDFFjL7mvdBx/qo7jyCXyE4fmMf7m/eyZPt+po5OrNMYtQcsx2VZ2X56X3Qbw/pmc2r/XqHjSA+QmZbM6P69WL2rlroEu329Clg6rbb+MF994kOaD+7nsjFF+m+/dJlxJfk0tzgrdlSHjhJTKmDpFHfnn55eTtm+OnY//59kpiaHjiQ9SN+cdEr6ZLKsrJrmBLp9vQpYOuXRt7bwl2U7ue/ykTTsWBU6jvRA40vyOdDQxMaqxBkrWAUsx/TKqgr+z4uruOK0Iu7WPd4kSoYWZJOXmcqH2/aHjhIzKmA5qhU7qvnakx9yenEeP71pAklJOu4r0WFmTCjNZ1dNPenFY0LHiQkVsBzR5t0H+cJjC8nPTOVXt04kM03HfSW6xgzIJTM1mdxzbggdJSZUwNKhjVUHuOnhd2hucR77wiT65WaEjiQJIDU5iTMG5ZE14hw2VNaGjhN1KmD5Oxsqa7l55ru0uPPEjMmMLNL5vhI74wbl03K4npnzN4WOEnUqYPkb89ZV8YlfvI07PPElla/EXmZaMgeWvcIzH+6goqY+dJyoUgEL0Hqe7yPzN3H7b95nYH4mz3z5PEaofCWQ2oXP0Nzi/OatLaGjRJUKWCjfX8cdjy/i+7NWc8Vp/Xnq7vMo6ZMVOpYksKbqCq48fQC/f3crtfU9975xKuAEdri5hd+9s4VpP5nPOxv38J1rxvDzT5+pW8pLXLhzyjBqG5p44v1toaNEjf6mJaDDzS0888EOHnx9A9v2HuKCU/ry7584XXu9ElfOGJTPucMKeHTBFj5/3lDSUnre/qIKOIGs3lnDMx/u4NkPd1BZ28DpxXn86taJTB3dTwPrSFyacdEwbv/NQp5fWs6NZw0KHafLqYB7qMamFjbtPsCq8hre3bSHtzfuoWxfHSlJxsWj+vHpc0q4ZJSKV+LbxSMLGVXUi5nzN3LDmcU9bntVAXdTdY3N7KqpZ+f+OnZW11O+v47y6jp27K9nx75DbNt7iMPNraNK5WWmMnlYH+68aDhXnz6APtlpgdOLdI6ZMWPKML7xp6W8urqSy8b0rAHbVcBxbt/BRhZv3cfqnTWsqzzAxsoD7KyuY9+hv/9muG9OGgPzMxnRrxeXj+nP6AG9GNW/FyP69SJZYzhIN3Xt+IHcP3cdD76+occdLlMBxxl3p6Kmgd6X3MEVP5nP2or/fznmoN6ZjOiXw5mD8xmQl8mAvAz652X89XGGxuiVHig1OYm7Lx7Ovzy7grc27OGCEX1DR+oyKuA4UdfYzPId1awor6a2voleZ11Dv9x0PjZuAGcP6cPY4jydHiYJ65MTB/HAa+v52WvrVcDSdQ40NPH+5r2s2llDc4tT2ieLycMK+PWMi/ldfeIMTC1yNOkpydw5ZTj/6y+reG/THs4ZVhA6UpdQAQdyuLmFD7btY/HWfTS3OKMH5DKhJJ+CnHQAvOFg4IQi8eWWSaX84o0NPPj6BhWwnLgd++qYs2oXNfVNnNIvh/OHF5CfpTMTRI4mMy2ZL144jB+8tIYl2/czviQ/dKST1vMuLYljTS0tLFi/mz9/UIaZccOZxVx9+gCVr0gnfXbyYPKzUnnwtfWho3SJIAVsZlvMbLmZLTGzRR0sNzP7mZltMLNlZnZmiJxd6WBDE08t3sHibfsYW5zLpyeVMqi3Lv0VOR456Sl84fyhvLK6skfcwj7kHvAl7j7e3Sd2sOxKYERkmgH8MqbJutiumnqeWLiNPQcbuOr0/kw9tahHXtcuEgu3nTeE3IwUfvrKutBRTlq8tsB1wG+91btAvpkNCB3qRGyqOsCfF5eRbMYnzyphRD+NsStyMvIyU5kxZRivrK7kw237Qsc5KaEK2IE5ZrbYzGZ0sLwY2N7meVlkXreyZlcNf1m+k745adx0dgmFvdJDRxLpET5//lD6ZKdx/9zuvRccqoDPd/czaT3U8BUzm9JueUfXGnpHb2RmM8xskZktqqqq6uqcJ2zFjmpeXlnBwLxMPjFhEFlpOuFEpKvkpKdw90XDeXP9bt7btCd0nBMWpIDdvTzysxJ4BpjUbpUyoKTN80FA+RHea6a7T3T3iYWFhdGIe9xW7azh1TWVDCnI4vrxA3W8VyQKPjt5MP16pfPjOetw73D/LO7FvBnMLNvMen30GJgGrGi32vPArZGzISYD1e6+M8ZRT8j6ylpeWVVBSZ9Mrj5jACnJKl+RaMhMS+aeS0/h/S17WbBhd+g4JyREOxQBC8xsKfA+8KK7zzazu8zsrsg6s4BNwAbgEeDLAXIet617DjJ7xS7652XwsTMGkpKk8hWJppvOLqE4P5MfddO94JgfmHT3TcC4DuY/1OaxA1+JZa6TVVXbwIvLd9InO43rxg0kVXu+IlGXnpLMvVNH8I9PLWPOqgquOK1/6EjHRS3RBQ40NPH80nLSU5K5blwx6RoWUiRmPnFmMcMLs/nh7DUcbm4JHee4qIBP0uHmFp5fWk5DUzPXjhtITobOdhCJpZTkJP7pytFsqjrIkwu3H/sFcUQFfBLcnVdWV1BV28CVYwfoPF+RQKaO7sc5Q/vw07nrqK3/+7vFxCsV8ElYsn0/6yoOcN7wAob2zQ4dRyRhmRnfvno0ew428tC8jaHjdJoK+ASV7TvEmxt2M7wwm4mDe4eOI5LwzhiUz3XjB/KrNzezs7oudJxOUQGfgAP1Tcxavov8zFQuH1PUo24SKNKd/Y9po3DgRy93j0uUVcDHqbnFeXH5TppaWrj69AGkp+iMB5F4UdIni9vPG8LTH5Z1i+EqVcDH6e2Nu9lVU8/lo4v+evsgEYkfX77kFHpnpfG9F1bG/cUZKuDjsG3vIT7Ytp/Ti/MYUaRhJUXiUV5mKt+cPoqFW/bx7JIdoeMclQq4k+oONzNn5S76ZKVxYQ+6LbZIXLIkzOyEp5snDaGhfC1f/fXrJKVnndR7tZ1KSgd36S9TVw10grvz6uoK6g+3cN34Yl1mLBJt3sL9c9ae1FtU1NTz5MLtXPeTuUwZ0TUjJd43bVSXvM9H1CSdsKK8ho1VBznvlAJdbCHSTRTlZjB2YC5Ltu9nz4GG0HE6pAI+hr0HG5m/rorSPllM6AG3wRZJJOcN70t6chJvrKuKyy/kVMBH0dzivLxyFynJpvN9RbqhzLRkzh1eQNm+OtZVHAgd5++ogI/inU17qKxt4LLRReSk63C5SHc0tjiPotx05q2roq6xOXScv6ECPoLtew+xeOs+xhbnMrwwJ3QcETlBSWZcNrqIhqZm5q+Pn/tGggq4Q3WHm3l51S56Z6V22benIhJO35x0Jg7pw5pdtWzZfTB0nL9SAbfz0SlndY3NTB/bX6ecifQQZw/pTZ/sNF5dU0ljU3wM3K52aWflR6ecDe9Lv14ZoeOISBdJSUristH9ONDQxFsb4+MmnirgNvYdamTeuipKemdyZml+6Dgi0sUG5GUyviSfZWXV7NgXfshKFXBEc4sze8UuUpKMaWP665QzkR7q3GEF5GWmMmfVLhqawp4VoQKO+OiUs6mji3RfN5EeLC0liWljiqitb2LeurBnRaiAaXPK2cBcTumnU85EerqB+ZmcPbQPq3fWsr6iNliOhC/gpIwc5qyqID8rlSkjdcqZSKKYNKQPRbnpvLqmMtiNPBO6gN2dPtO/yqHGJqafplPORBJJcpJxxWn9aXFn7qqKIGNFJHTj/GlRGdmjzufc4QUU5eqUM5FE0zsrjSkjCtm+r47F2/bF/PMTtoBbWpwnFm6jfutSzirVXY1FEtVpA3MZ0S+HtzfuoWzfoZh+dsIWcFKS8cSXJlP13A91yplIAjMzpo7uR15mKi+t2MXBhqaYfXbMC9jMSszsdTNbbWYrzezeDta52MyqzWxJZPpuNLJkpCbTUlcTjbcWkW4kPSWZq08fQGNTC7NW7KS5JTbHg0PsATcB33D30cBk4CtmNqaD9d509/GR6X/FNqKIJJq+OelMHd2P8v31vB2jS5VjXsDuvtPdP4g8rgVWA8WxziEi0t6p/XM5oziPD7btj8n5wUGPAZvZEGAC8F4Hi881s6Vm9pKZnXaU95hhZovMbFFVVXyN9Ski3c+FI/vSPzeDOasqqKipj+pnBStgM8sBngK+7u7tD8R+AAx293HAA8CzR3ofd5/p7hPdfWJhoS6kEJGTk5KUxDVnDCAzLZkXlpZH9SKNIAVsZqm0lu/v3f3p9svdvcbdD0QezwJSzaxvjGOKSILKTk/h2nEDOdzsvLB0Z9TGDw5xFoQBvwZWu/v9R1inf2Q9zGwSrTn3xC6liCS6vjnpXDm2P7sPNPDyyl20ROFKuRDDfp0PfA5YbmZLIvP+GSgFcPeHgBuBu82sCagDbvZ4vKe0iPRoQ/pmM2VkIfPWVbFgfdefGRHzAnb3BcBRr3xw9weBB2OTSETkyMYNyqP60GE+3L6f3Ekf79L3Ttgr4UREOsPMmDKyLyP65ZA76RNU13Xdl3IqYBGRYzAzpp1WxM7ffoO8zNQue1/d+iFeWZLGqBCJIylJSTTXVHbte3bpu0nX8Rbun7M2dIoO3TdtVOgIIj2CDkGIiASiAhYRCUQFLCISiApYRCQQFbCISCAqYBGRQFTAIiKBqIBFRAJRAYuIBKICFhEJRAUsIhKIClhEJBAVsIhIICpgEZFAVMAiIoGogEVEAlEBi4gEogIWEQlEBSwiEogKWEQkEBWwiEggKmARkUBUwCIigaiARUQCCVLAZjbdzNaa2QYz+1YHy83MfhZZvszMzgyRU0QkmmJewGaWDPwcuBIYA9xiZmParXYlMCIyzQB+GdOQIiIxEGIPeBKwwd03uXsj8CRwXbt1rgN+663eBfLNbECsg4qIRJO5e2w/0OxGYLq7fzHy/HPAOe5+T5t1/gL8wN0XRJ6/CnzT3Rd18H4zaN1LBhgFrI3yL6EjfYHdAT433jJAfOSIhwwQHzniIQPER46QGXa7+/T2M1MCBLEO5rX/V6Az67TOdJ8JzDzZUCfDzBa5+8REzxAvOeIhQ7zkiIcM8ZIjHjK0F+IQRBlQ0ub5IKD8BNYREenWQhTwQmCEmQ01szTgZuD5dus8D9waORtiMlDt7jtjHVREJJpifgjC3ZvM7B7gZSAZeNTdV5rZXZHlDwGzgKuADcAh4PZY5zxOQQ+BRMRDBoiPHPGQAeIjRzxkgPjIEQ8Z/kbMv4QTEZFWuhJORCQQFbCISCAq4E4wsxIze93MVpvZSjO79yjrnm1mzZHznYPkMLOLzWxJZJ15IXKYWZ6ZvWBmSyPrdOlxfDPLMLP327z/9zpYJ+qXtHcyx2cin7/MzN42s3GxztBm3Whun53KEc3ts5N/HlHdNo+Lu2s6xgQMAM6MPO4FrAPGdLBeMvAarV8i3hgiB5APrAJKI8/7Bcrxz8API48Lgb1AWhdmMCAn8jgVeA+Y3G6dq4CXIutOBt6Lwu9FZ3KcB/SOPL6yq3N0JkOMts/O/F5EdfvsZIaobpvHM2kPuBPcfae7fxB5XAusBoo7WPWrwFNAZcAcnwaedvdtkfW6PEsnczjQy8wMyKF1I2/qwgzu7gciT1MjU/tvlKN+SXtncrj72+6+L/L0XVrPa49phohob5+dyRHV7bOTGaK6bR4PFfBxMrMhwARa/2VtO78Y+DjwUMgcwEigt5m9YWaLzezWQDkeBEbTegHNcuBed2/p4s9ONrMltBbKXHdvn6EY2N7meRkd/8MZ7Rxt3UHrXnlMM8Rq++zE70XUt89OZIj6ttlZKuDjYGY5tO5BfN3da9ot/imt41U0B86RApwFXA1cAXzHzEYGyHEFsAQYCIwHHjSz3K78fHdvdvfxtO5RTjKzse0jdvSyrszQyRytYcwuobWAvxkgw0+JwfbZiRxR3z47kSHq22ZnqYA7ycxSaS2b37v70x2sMhF40sy2ADcCvzCz6wPkKANmu/tBd98NzAe69EufTua4ndb/arq7bwA2A6d2dQ4Ad98PvAG0H+wkppe0HyUHZnYG8CvgOnffEyBDTLbPTuSIyfZ5jAwx2zaPRQXcCZFjRb8GVrv7/R2t4+5D3X2Iuw8B/gx82d2fjXUO4DngQjNLMbMs4Bxaj9HGOsc2YGpk/SJaR6rb1IUZCs0sP/I4E7gMWNNutahf0t6ZHGZWCjwNfM7d13Xl53c2Q4y2z878mUR1++xkhqhum8cjxGho3dH5wOeA5ZFjS9D6TWop/PXy6bjI4e6rzWw2sAxoAX7l7itinQP438BjZrac1kMB34zs8XSVAcDj1jrAfxLwR3f/i8X+kvbO5PguUEDrXidAk3ftqFydyRALx8wRg+2zM78X0d42O02XIouIBKJDECIigaiARUQCUQGLiASiAhYRCUQFLCISiApYEpKZFZnZf5vZpsglse+Y2ccjI3VVm9mH1jra27+2ec0EM3MzuyJkduk5VMCScCIXkjwLzHf3Ye5+Fq33JvxokJw33X0CrVePfdbMzorMvwVYEPkpctJUwJKILgUa216g4O5b3f2Btiu5+0FgMTA8Uto3Ap8HpplZRgzzSg+lApZEdBrwwbFWMrMCWscRXknr1X+b3X0jreMLXBXNgJIYVMCS8Mzs59Z6d4SFkVkXmtmHwBzgB+6+ktbDDk9Glj+JDkNIF9ClyJJwzGwq8F13v6jNvL7AIloPMfwPd7+mzbJkYAdwGGimdfyAAmCAtw5IL3JCtAcsieg1IMPM7m4zL+so618GLHX3ksiIYoNpHYrz+ihmlASgApaE463/7bseuMjMNpvZ+8DjHHmg9FuAZ9rNe4rW2+uInDAdghARCUR7wCIigaiARUQCUQGLiASiAhYRCUQFLCISiApYRCQQFbCISCD/D6XBO2iKPKLnAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.displot(new_stu[\"GPA\"], kde = True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.displot(new_stu[\"Salary\"],kde = True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.displot(new_stu[\"Spending\"], kde = True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.displot(new_stu[\"Text Messages\"], kde = True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# From the above plots, we can observe the distribution of the four variables. We can see that GPA and Salary follow a normal distribution while Spending and Text Messages show a bit of right skweness in data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.8.2 Write a note summarizing your conclusions for this whole Problem 2.\n",
    "# Refer Docs"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Problem 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "An important quality characteristic used by the manufacturers of ABC asphalt shingles is the amount of moisture the shingles contain when they are packaged. Customers may feel that they have purchased a product lacking in quality if they find moisture and wet shingles inside the packaging.   In some cases, excessive moisture can cause the granules attached to the shingles for texture and colouring purposes to fall off the shingles resulting in appearance problems. To monitor the amount of moisture present, the company conducts moisture tests. A shingle is weighed and then dried. The shingle is then reweighed, and based on the amount of moisture taken out of the product, the pounds of moisture per 100 square feet is calculated. The company would like to show that the mean moisture content is less than 0.35 pound per 100 square feet.\n",
    "\n",
    "The file (A & B shingles.csv) includes 36 measurements (in pounds per 100 square feet) for A shingles and 31 for B shingles."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "shi = pd.read_csv(\"A & B shingles-1.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "A    11.40\n",
       "B     8.48\n",
       "dtype: float64"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "shi.sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.44</td>\n",
       "      <td>0.14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.61</td>\n",
       "      <td>0.15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.47</td>\n",
       "      <td>0.31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.30</td>\n",
       "      <td>0.16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.15</td>\n",
       "      <td>0.37</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      A     B\n",
       "0  0.44  0.14\n",
       "1  0.61  0.15\n",
       "2  0.47  0.31\n",
       "3  0.30  0.16\n",
       "4  0.15  0.37"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "shi.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>0.40</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>0.29</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>0.43</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>0.34</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>0.37</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       A   B\n",
       "31  0.40 NaN\n",
       "32  0.29 NaN\n",
       "33  0.43 NaN\n",
       "34  0.34 NaN\n",
       "35  0.37 NaN"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "shi.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>A</th>\n",
       "      <td>36.0</td>\n",
       "      <td>0.316667</td>\n",
       "      <td>0.135731</td>\n",
       "      <td>0.13</td>\n",
       "      <td>0.2075</td>\n",
       "      <td>0.29</td>\n",
       "      <td>0.3925</td>\n",
       "      <td>0.72</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>B</th>\n",
       "      <td>31.0</td>\n",
       "      <td>0.273548</td>\n",
       "      <td>0.137296</td>\n",
       "      <td>0.10</td>\n",
       "      <td>0.1600</td>\n",
       "      <td>0.23</td>\n",
       "      <td>0.4000</td>\n",
       "      <td>0.58</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   count      mean       std   min     25%   50%     75%   max\n",
       "A   36.0  0.316667  0.135731  0.13  0.2075  0.29  0.3925  0.72\n",
       "B   31.0  0.273548  0.137296  0.10  0.1600  0.23  0.4000  0.58"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "shi.describe().T"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 3.1 Do you think there is evidence that means moisture contents in both types of shingles are within the permissible limits? State your conclusions clearly showing all steps."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#3.1\n",
    "\n",
    "Constructing Hypothesis: \n",
    "\n",
    "H0 : Mean Moisture content of Shingles = 0.35 (or can be written as >= 0.35)\n",
    "\n",
    "H1 : Mean Moisture content of Shingles < 0.35\n",
    "\n",
    "Level of significance:\n",
    "alpha = 0.05\n",
    "\n",
    "Test conditions: \n",
    "Since the two samples are independent, we conduct individual tests on each type of shingles.\n",
    "The test conducted will be a One tail test.\n",
    "The population standard deviation is unknown.\n",
    "\n",
    "One Sample T-test formula : \n",
    "\n",
    "t = (Xbar - mu(expected value))/(s/sqrt(n))\n",
    "\n",
    "\n",
    "If P value > alpha , null hypothesis is not rejected\n",
    "\n",
    "If P value < alpha , null hypothesis is rejected which means the mean moisture content both types of Shingles are within the permissible limits "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "A    0.018423\n",
       "B    0.018850\n",
       "dtype: float64"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "shi.var() #sample variance "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Calculating the T stat and P value of Shingle type A"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tstat: -1.6005252585398313\n",
      "P_Value_A: 0.11996170801033942\n"
     ]
    }
   ],
   "source": [
    "t_statistic, p_value_A = ttest_1samp(shi_na[\"A\"], 0.35)\n",
    "print('tstat:',t_statistic)    \n",
    "print('P_Value_A:',p_value_A) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [],
   "source": [
    "# P_value > alpha \n",
    "\n",
    "# Since, P value > alpha , null hypothesis is not rejected\n",
    "\n",
    "# Hence the mean moisture content of the Shingles A is not within the permissible limit of 0.35"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "shi_B = shi[\"B\"].dropna()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Sample Size of B: 31 "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Calculating the T stat and P value of Shingle type B"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tstat: -3.1003313069986995\n",
      "P_Value_B: 0.004180954800638363\n"
     ]
    }
   ],
   "source": [
    "t_statistic, p_value_B = ttest_1samp(shi_B, 0.35)\n",
    "print('tstat:',t_statistic)    \n",
    "print('P_Value_B:',p_value_B) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# P_value > alpha \n",
    "\n",
    "# Since, P value > alpha , null hypothesis is not rejected\n",
    "\n",
    "# Hence the mean moisture content of the Shingles A is not within the permissible limit of 0.35"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can conclude that at 95% there is sufficient evidence to prove that the type 'A' shingles have a mean moisture content which is less than the permissible limit of 0.35 and type 'B' shingles have a mean moisture content that lies within the given limit"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 3.2 Do you think that the population means for shingles A and B are equal? Form the hypothesis and conduct the test of the hypothesis. What assumption do you need to check before the test for equality of means is performed?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#3.2 \n",
    "\n",
    "Hypothesis: \n",
    "\n",
    "H0 : uA = uB\n",
    "\n",
    "Ha : uA not equal to uB\n",
    "\n",
    "Two Tailed test\n",
    "\n",
    "Assumptions that the variance are equal\n",
    "\n",
    "Since the variances of both the samples are equal and the mean of the population is unknown, we conduct a Two sample T-test: "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Two sample T-Test: \n",
    "\n",
    "t = (x1_bar - x2_bar)/sqrt((s1**2)/n1 + (s2**2)/n2) \n",
    "\n",
    "\n",
    "x1_bar = 0.316667\n",
    "x2_bar = 0.273548\n",
    "\n",
    "n1 = 36\n",
    "n2 = 31\n",
    "\n",
    "s1 = 0.135731\n",
    "s2 = 0.137296  \n",
    "\n",
    "\n",
    "alpha = 0.05\n",
    "dof= 65"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [],
   "source": [
    "x1_bar = 0.316667\n",
    "x2_bar = 0.273548"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "s1 = 0.135731\n",
    "s2 = 0.137296    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Since B has null values, we can drop those inorder to calculate\n",
    "shi_B = shi[\"B\"].dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {},
   "outputs": [],
   "source": [
    "n1 = 36\n",
    "n2 = 31\n",
    "dof = n1 + n2 - 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tstat: 1.289628271966112\n",
      "p_Value: 0.2017496571835328\n"
     ]
    }
   ],
   "source": [
    "t_statistic, p_value  = ttest_ind(shi['A'],shi_B)\n",
    "print('tstat:',t_statistic)    \n",
    "print('p_Value:',p_value) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# P_value > alpha \n",
    "\n",
    "# Since, P value > alpha , null hypothesis is not rejected\n",
    "\n",
    "# Hence we can conclude that at 95% there is sufficient evidence to prove that the population mean of the Shingles A and Shingles B are equal"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
