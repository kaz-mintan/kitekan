import numpy as np

#//1〜10種類ある予測関数番号をもらうと計算をする関数を作ります
def func(factor, mental, func_num):
  if func_num == 0:
    ret = 1.0 / (1.0 + np.exp(mental*(factor / 80.0 - 0.4)))*(mental + 1) / 11.0#//試行回数・happy
  if func_num == 1:
    ret = 1.0 / (1.0 + np.exp(mental*(factor / 80.0 - 0.6)))*0.6*((mental + 1.0) / 11.0)##//試行回数sup
  if func_num == 2:
    ret = 1.0 / (1.0 + np.exp(-2.0*(10 - mental)*(factor / 80.0 - 0.2)))*0.8*((11.0 - mental) / 11.0)#//試行回数ang
  if func_num == 3:
    ret= np.exp(-(factor / 80 - 0.3)*(factor / 80.0 - 0.3) / 0.02)*(mental + 1.0 / 11.0)#//試行回数sad

  if func_num == 4:
    ret= np.exp((factor / 100.0 - 1.0) / mental*8.0)*mental / 10.0#//正答率happy
  if func_num == 5:
    ret= np.exp((factor / 100.0 - 1.3) / mental*8.0)*mental / 10.0#//正答率sup
  if func_num == 6:
    ret= np.exp(-(factor / 100.0 + 0.15) / (11 - mental)*7.0)#//正答率ang
  if func_num == 7:
    ret= np.exp(-(factor / 100.0 + 0.3) / (11 - mental)*7.0)#//正答率sad

  if func_num == 8:
    ret= 0.6*mental / 11.0*np.exp(-(factor - 0.3)*(factor - 0.3) / 0.05)#//励ましhap
  if func_num == 9:
    ret= mental / 10.0*np.exp(8.0*(factor - 1.5) / mental) + 0.05#//励ましsup
  if func_num == 10:
    ret= np.exp(-(factor + 0.3) / (11.0 - mental)*7.0) + 0.1#//励ましang
  if func_num == 11:
    ret= np.exp(-7 * (factor + 0.3) / (11.0 - mental))#//励ましsad

  if func_num == 12:
    ret= (mental + 1.0) / 11.0*0.7*np.exp(-(factor - 0.35)*(factor - 0.35) / 0.1)#//共感happy
  if func_num == 13:
    ret= np.exp((factor - 1.5) / mental * 10)*mental / 10.0 + 0.05#//共感sup
  if func_num == 14:
    ret= np.exp((factor + 0.3) / (11 - mental)*7.0) + 0.1#//共感ang
  if func_num == 15:
    ret= np.exp((factor + 0.3) / (11 - mental)*7.0)#//共感sad

  if func_num == 16:
    ret= np.exp(-(factor + 0.2) / mental*10.0)*0.3#//からかいhappy
  if func_num == 17:
    ret= np.exp(-(factor + 0.1) / mental*10.0)*0.4#//からかいsup
  if func_num == 18:
    ret= np.exp((factor - 1.0) / (11.0 - mental)*10.0)*(11.0 - mental) / 11 + 0.1#//からかいang
  if func_num == 19:
    ret= np.exp((factor - 1.2) / (11.0 - mental)*20.0)*(11.0 - mental) / 11 + 0.05#//からかいsad

  if func_num == 20:
    ret= np.exp(-(factor + 0.2) / mental*10.0)*0.2#//関係ないhap
  if func_num == 21:
    ret= np.exp(-(factor + 0.1) / mental*10.0)*0.3#//関係ないsup
  if func_num == 22:
    ret= np.exp((factor - 1.0) / (11.0 - mental)*20.0)*(11.0 - mental) / 11.0#//関係ないang
  if func_num == 23:
    ret= np.exp((factor - 1.2) / (11.0 - mental)*30.0)*(11.0 - mental) / 11.0#//関係ないsad

  if func_num == 24:
    ret= np.exp(-(factor + 0.2) / mental*10.0)*2.0#//行動なしhap
  if func_num == 25:
    ret= np.exp((factor - 1.3) / mental*20.0)*mental / 11.0#//行動なしsup
  if func_num == 26:
    ret= np.exp((factor - 1.0) / (11.0 - mental)*20.0)*(11.0 - mental) / 11.0#//行動なしang
  if func_num == 27:
    ret= np.exp((factor - 1.1) / (11.0 - mental)*20.0)*(11.0 - mental) / 11.0#//行動なしsad

  if func_num == 28:
    ret= ((mental + 1.0) / 11.0) / (1.0 + np.exp(-mental*(factor / 240.0 - 0.5)))#//獲得点数happy
  if func_num == 29:
    ret= ((mental + 1.0) / 11.0) / (1.0 + np.exp(-mental*(factor / 320.0 - 0.2)))*0.5 + 0.3#//獲得点数sup
  if func_num == 30:
    ret= 1.0 / (1.0 + np.exp(3.0*mental*(factor / 320.0 + 0.15)))#//獲得点数ang
  if func_num == 31:
    ret= 0.7 / (1.0 + np.exp(mental*(factor / 320.0 + 0.15)))#//獲得点数sad

  if func_num == 32:
    ret= ((mental + 1.0) / 11.0)*0.6 / (1.0 + np.exp(-2 * mental*(factor / 80.0 - 0.2))) + 0.2#//連勝数happy
  if func_num == 33:
    ret= ((mental + 1.0) / 11.0)*0.7 / (1.0 + np.exp(-mental*(factor / 80.0 - 0.3))) + 0.1#//連勝数sup
  if func_num == 34:
    ret= np.exp(-(factor / 80 + 2.0) / (11.0 - mental)*10.0)#//連勝数ang
  if func_num == 35:
    ret= np.exp(-(factor / 80 + 3.0) / (11.0 - mental)*10.0)#//連勝数sad

  if func_num == 36:
    ret= np.exp(-(factor / 80 + 3.0) / (11.0 - mental)*10.0)#//連敗数hap
  if func_num == 37:
    ret= np.exp(-(factor / 80 + 2.0) / (11.0 - mental)*10.0) + 0.1#//連敗数sup
  if func_num == 38:
    ret= ((11.0 - mental) / 11.0)*0.4 / (1.0 + np.exp(-(11.0 - mental)*(factor / 80.0 - 0.6))) + 0.4#//連勝数ang
  if func_num == 39:
    ret= ((11.0 - mental) / 11.0)*0.4 / (1.0 + np.exp(-(11.0 - mental)*(factor / 80.0 - 0.4))) + 0.4#//連勝数sad
  return ret
"""
#//1〜10種類ある予測関数番号をもらうと計算をする関数を作ります
double func2(double factor,double mental, int func_num){
  if func_num == 0:
    ret= 2.0/(1.0+np.exp((factor/80.0-0.15-mental/50.0)*30.0))-1.0#
  if func_num == 1:
    ret= (pow((factor+1.0),(11.0-mental))-1.0)/(pow(2.0,(11.0-mental))-1.0)*2.0-1.0#
  if func_num == 2:
    ret= -np.exp(-factor*factor/((11.0-mental)/500.0))+np.exp(-(factor-0.5)*(factor-0.5)/(mental/300.0))#
  if func_num == 3:
    ret= -np.exp(-factor*factor/((11.0-mental)/500.0))+np.exp(-(factor-0.5)*(factor-0.5)/(mental/300.0))#
  if func_num == 4:
    ret= (pow(2.0,(11.0-mental)*0.8)/(pow(2.0,(11.0-mental)*0.8)-1.0)/pow((factor/80.0+1.0),(0.8*(11.0-mental)))-1.0/(pow(2.0,(0.8*(11.0-mental)))-1))*2.0-1.0#
  if func_num == 5:
    ret= np.exp(-(factor-0.2)*(factor-0.2)/(mental/700.0))-np.exp(-(factor-0.7)*(factor-0.7)/((11.0-mental)/300.0))#
  if func_num == 6:
    ret= np.exp(-factor*factor/(mental/600.0))-np.exp(-(factor-0.5)*(factor-0.5)/((11.0-mental)/200.0))#
  if func_num == 7:
    ret= 2.0/(1.0+np.exp(-35.0*(factor/240.0-0.2+mental/50.0)))-1.0#
  if func_num == 8:
    ret= (pow((factor/80.0+1.0),(9.0*(11.0-mental)))-1.0)/(pow(2.0,(9.0*(11.0-mental)))-1.0)#
  if func_num == 9:
    ret= 1.0/(1.0+np.exp(50.0*(factor/80.0-0.1-mental/50.0)))-1.0#
  if func_num == 10:
    ret= 0.2/(1.0+np.exp(10.0*mental))-0.1##//心的状態弾性
}
"""
