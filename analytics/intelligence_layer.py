import pandas as pd
import json
from datetime import datetime

# Load dataset
df = pd.read_csv("data/new_data.csv")

def generate_intelligence_contract(df):

    # Market Trend
  
    avg_close = df["close"].mean()
    avg_open = df["open"].mean()

    if avg_close > avg_open:
        market_trend = "BULLISH"
    else:
        market_trend = "BEARISH"

    # Volatility Detection

    volatility = df["close"].std()

    if volatility > 50:
        volatility_level = "HIGH"

    elif volatility > 20:
        volatility_level = "MODERATE"

    else:
        volatility_level = "LOW"

    
    # Volume Behavior

    avg_volume = df["volume"].mean()
    latest_volume = df["volume"].iloc[-1]

    if latest_volume > avg_volume * 2:
        volume_behavior = "ABNORMAL"
        abnormal_volume_detected = True

    else:
        volume_behavior = "NORMAL"
        abnormal_volume_detected = False

    
    # Momentum Signal
    
    recent_close = df["close"].iloc[-1]
    old_close = df["close"].iloc[-5]

    if recent_close > old_close:
        momentum_signal = "POSITIVE"

    else:
        momentum_signal = "NEGATIVE"

    
    # Price Spike Detection
    
    daily_change = (df["close"] - df["open"]).abs().max()

    if daily_change > 100:
        price_spike_detected = True
    else:
        price_spike_detected = False


    # Intelligence Contract
    
    intelligence_contract = {

        "schema_version": "1.0.0",

        "request_id": "INTELLIGENCE-LAYER-001",

        "timestamp_utc": datetime.utcnow().isoformat(),

        "market_intelligence": {

            "market_trend": market_trend,

            "volatility_level": volatility_level,

            "volume_behavior": volume_behavior,

            "momentum_signal": momentum_signal
        },

        "risk_signals": {

            "high_volatility_detected": bool(volatility > 50),

            "abnormal_volume_detected": bool(abnormal_volume_detected),

            "price_spike_detected": bool(price_spike_detected)
        },

        "statistical_intelligence": {

            "average_close_price": float(df["close"].mean()),

            "average_daily_movement": float(
                (df["close"] - df["open"]).mean()
            ),

            "rolling_average_window": 7,

            "rolling_average_value": float(
                df["close"].rolling(7).mean().iloc[-1]
            )
        },

        "deterministic_observations": [

            "Market intelligence generated successfully",

            "Statistical analysis completed",

            "Risk signal evaluation completed"
        ],

        "execution_status": {

            "status": "SUCCESS",

            "intelligence_layer_execution": "COMPLETED"
        }
    }

    # Save JSON file
    with open("exports/intelligence_contract.json", "w") as file:
        json.dump(intelligence_contract, file, indent=4)
    
    print( "Market intelligence generated..")
    print( "Statistical analysis completed")
    print("Risk signal evaluation completed")
    print("Intelligence contract generated successfully.\n")

    return df

