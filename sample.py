def car_speed(speed):
    if speed < 0 :
      return ("Level shall be Invalid")
    if speed >= 0 and speed <= 40:
      return ("Level shall be Low")
    if speed >= 40 and speed <= 120:
      return ("Level shall be Normal")
    if speed > 120 and speed <= 200:
      return ("Level shall be High")
    if speed >= 200 and speed < 220:
      return ("Level shall be V.High")
    if speed > 220:
      return ("Level shall be Invalid")

def student_score(score):
    if score < 0 :
      return ("Level shall be Invalid")
    if score >= 0 and score <= 50:
      return ("Level shall be Low")
    if score >= 50 and score <= 65:
      return ("Level shall be Normal")
    if score > 65 and score <= 75:
      return ("Level shall be High")
    if score >= 75 and score < 85:
      return ("Level shall be V.High")
    if score >= 85 and score < 100:
      return ("Level shall be Excellent")
    if score > 100:
      return ("Level shall be Invalid")