from src.privacy_guard.privacy import PrivacyGuard

guard = PrivacyGuard()

text = """
Hi, my name is Ali.
My email is ali@example.com
My phone is +98 912 123 4567
Visit https://example.com
I feel hopeless and alone.
"""

result = guard.process(text)

print("=== ORIGINAL ===")
print(result["original_text"])

print("=== ANONYMIZED ===")
print(result["anonymized_text"])

print("=== ENTITIES ===")
print(result["detected_entities"])

print("=== COUNT ===")
print(result["entity_count"])