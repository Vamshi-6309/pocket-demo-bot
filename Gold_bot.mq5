#property strict
#include <Trade/Trade.mqh>

CTrade trade;

input double LotSize = 0.01;
input int TakeProfitPips = 300;
input ENUM_TIMEFRAMES Timeframe = PERIOD_M15;

datetime lastBar = 0;

// Basic starter EA: detects a two-candle breakout pattern.
// This is NOT yet the complete locked breakout-retest strategy.

void OnTick()
{
   datetime currentBar = iTime(_Symbol, Timeframe, 0);
   if(currentBar == 0 || currentBar == lastBar)
      return;

   lastBar = currentBar;

   if(PositionSelect(_Symbol))
      return;

   double open1  = iOpen(_Symbol, Timeframe, 2);
   double close1 = iClose(_Symbol, Timeframe, 2);
   double high1  = iHigh(_Symbol, Timeframe, 2);
   double low1   = iLow(_Symbol, Timeframe, 2);

   double open2  = iOpen(_Symbol, Timeframe, 1);
   double close2 = iClose(_Symbol, Timeframe, 1);

   if(open1 == 0 || open2 == 0)
      return;

   // Basic BUY breakout pattern
   if(close1 < open1 && close2 > open2 && close2 > high1)
   {
      double ask = SymbolInfoDouble(_Symbol, SYMBOL_ASK);
      double sl = low2_placeholder();
      double tp = ask + TakeProfitPips * _Point;

      // Intentionally no order placement until SL/TP
      // and broker-specific gold pip rules are verified.
      Print("BUY pattern detected. Verify retest and SL before trading.");
   }

   // Basic SELL breakout pattern
   if(close1 > open1 && close2 < open2 && close2 < low1)
   {
      Print("SELL pattern detected. Verify retest and SL before trading.");
   }
}

double low2_placeholder()
{
   return iLow(_Symbol, Timeframe, 1);
}
