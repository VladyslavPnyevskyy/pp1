text = "X-DSPAM-Confidence: 0.8475"
start = text.find(":")
line = text[start+1:]
floatLine = float(line.strip())
print(f"number is: {floatLine}")