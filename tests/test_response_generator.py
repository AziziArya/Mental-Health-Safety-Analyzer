from src.response_generator.generator import SafetyResponseGenerator

generator = SafetyResponseGenerator()


decision = {"final_risk_score": 0.85, "final_risk_level": "High Risk"}


result = generator.generate(decision, "I feel alone")


print("\n=== RESPONSE GENERATOR TEST ===")

print(result)


assert "message" in result

assert "response_type" in result

assert "priority" in result


print("\nRESPONSE GENERATOR TEST PASSED")
