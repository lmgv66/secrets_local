import requests

def myfunction():
    invalido="xya_eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJuYXVpayIsImlhdCI6MTY2NzQwNDI2NiwiZXhwIjoxNjY5OTk2MjY2LCJhcGl0b2tlbmRhdGEiOnsidXNlckJlYW4iOnsiaWQiOjEsIm5hbWUiOiJuYXVpa191c2VyIiwibG9naW4iOiJuYXVpayIsInBhc3N3b3JkIjoiJDJhJDEyJGpOckI4MGs5MnJVdmxQMzhhTE9OYWVPb3RFWWl3VmQ1TWFDN043TDQ0Y0dYRjQueXJxLm9hIiwiY3VzdG9tZXJJZCI6MSwiYXV0aG9yaXRpZXMiOlt7ImF1dGhvcml0eSI6IlJPTEVfUk9PVCJ9XSwiZW5hYmxlZCI6ZmFsc2UsInByb2plY3RJZHMiOlsxLDIsMyw0LDYsNyw4LDksMTEsMTIsMTMsMTQsMTUsMTcsMTgsMTldLCJ1c2VybmFtZSI6Im5hdWlrIiwiYWNjb3VudE5vbkV4cGlyZWQiOnRydWUsImFjY291bnROb25Mb2NrZWQiOnRydWUsImNyZWRlbnRpYWxzTm9uRXhwaXJlZCI6dHJ1ZX0sInRva2VuSWQiOjV9fQ.F89ZjeeVgzqwd50BJUrK0SsRztQMECsSpvofw21uTDOeXc38227pC4to-X6A3avDZYkC-050GNIB_GNQLg6YwQ"
    # xygeni
    valid3="xya_eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJsdWlzLmdhcmNpYUB4eWdlbmkuaW8iLCJpYXQiOjE3MjA3NjYxNzcsImV4cCI6MTcyODU0MjE3NywiYXBpdG9rZW5kYXRhIjp7InVzZXJCZWFuIjp7ImlkIjo3MCwibmFtZSI6Ikx1aXMgUHJvIiwibG9naW4iOiJsdWlzLmdhcmNpYUB4eWdlbmkuaW8iLCJjdXN0b21lcklkIjoyMCwibWZhIjpmYWxzZSwibWZhQWxsIjpmYWxzZSwiYXV0aG9yaXRpZXMiOlt7ImF1dGhvcml0eSI6IlJPTEVfUk9PVCJ9XSwiZW5hYmxlZCI6ZmFsc2UsImNoYW5nZWRQYXNzd29yZCI6ZmFsc2UsImN1c3RvbWVyT3duZXIiOnRydWUsImFjY291bnROb25FeHBpcmVkIjp0cnVlLCJhY2NvdW50Tm9uTG9ja2VkIjp0cnVlLCJjcmVkZW50aWFsc05vbkV4cGlyZWQiOnRydWUsIm1mYUVuYWJsZWQiOmZhbHNlLCJzdGFydFN1YnNjcmlwdGlvbiI6MTcxMDkyMjg3MTAwMCwiZW5kU3Vic2NyaXB0aW9uIjoxNzQyMDI2ODcxMDAwLCJwcm9qZWN0SWRzIjpbXSwiZmVhdHVyZXMiOltdLCJlYXJseUFjY2VzcyI6ZmFsc2UsInVzZXJuYW1lIjoibHVpcy5nYXJjaWFAeHlnZW5pLmlvIn0sInRva2VuSWQiOjE0MH19.K9iVNQYmNwmP8gRDTVx1-JS_wRMmaCPBjifmemjZDg7SLVw7iu1clSKPVLhnUFvb7VMOJo4YRzh_A4RinVwPJA";
    valid4_toexpire="xya_eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJsdWlzLmdhcmNpYUB4eWdlbmkuaW8iLCJpYXQiOjE3MjE2MzQyNDIsImV4cCI6MTcyMTcyMDY0MiwiYXBpdG9rZW5kYXRhIjp7InVzZXJCZWFuIjp7ImlkIjo3MCwibmFtZSI6Ikx1aXMgUHJvIiwibG9naW4iOiJsdWlzLmdhcmNpYUB4eWdlbmkuaW8iLCJjdXN0b21lcklkIjoyMCwibWZhIjpmYWxzZSwibWZhQWxsIjpmYWxzZSwiYXV0aG9yaXRpZXMiOlt7ImF1dGhvcml0eSI6IlJPTEVfUk9PVCJ9XSwiZW5hYmxlZCI6ZmFsc2UsImNoYW5nZWRQYXNzd29yZCI6ZmFsc2UsImN1c3RvbWVyT3duZXIiOnRydWUsImFjY291bnROb25FeHBpcmVkIjp0cnVlLCJhY2NvdW50Tm9uTG9ja2VkIjp0cnVlLCJjcmVkZW50aWFsc05vbkV4cGlyZWQiOnRydWUsIm1mYUVuYWJsZWQiOmZhbHNlLCJzdGFydFN1YnNjcmlwdGlvbiI6MTcxMDkyMjg3MTAwMCwiZW5kU3Vic2NyaXB0aW9uIjoxNzQyMDI2ODcxMDAwLCJwcm9qZWN0SWRzIjpbXSwiZmVhdHVyZXMiOltdLCJlYXJseUFjY2VzcyI6ZmFsc2UsInVzZXJuYW1lIjoibHVpcy5nYXJjaWFAeHlnZW5pLmlvIn0sInRva2VuSWQiOjE0M319.rjzcIczc9gfE44RDvBTDz3AyM-ysOu5npfO4nwICzWiNmhd89qb35exkAs4VLO4hU-c-P44M4h0thT2gRKxzUQ";
