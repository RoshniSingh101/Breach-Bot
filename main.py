#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts start of Breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Facebook breach in 2019!")

#Introduces Breach
print("Would you like to learn more about the 2019 Facebook Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains Breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) Facebook's response, or (c) What's your opinion on the data breach?")
  topic = input()
  
  if topic.lower() == "a":
    print("In August 2019, malicious actors stole personal data from 530 million Facebook users in 106 different countries after finding a vulnerability in the platform’s former feature of connecting users by providing their phone numbers to be readily available. Facebook later reached a $5 billion settlement with the U.S. Federal Trade Commission for violating its agreement with the agency to protect user privacy.")
  
  elif topic.lower() == "b":
    print("A Facebook spokesperson told NPR that Facebook was not going to notify users individually if malicious actors stole their personal information anytime soon. Because public information is widely open to scammers and hackers on the web, Facebook does not believe that users can fix the issue. To prevent a data breach however, cybersecurity experts strongly suggest users to use two-factor authentication via text messages or email to verify their identities.")
  
  elif topic.lower() == "c":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

#Introduces Breach Bot's Opinion on the Breach
print("I'm excited to share my perspective with you. Are you ready to hear my opinion on the 2019 Facebook Data Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares Breach Bot's Opinion on the Breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relations to the CIA Triad, (b) my opinion on the 2019 Facebook Data Breach, (c) my advice to protect yourself from future data breaches, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("Malicious actors stole personal information from 530 millions Facebook users from 106 different countries, aligning with confidentiality because malicious actors violated user privacy and Facebook did not take action to protect the information of their clients to ensure their safety and security on the web.")
  
  elif topic.lower() == "b":
    print("I disagree with the organization's response because Facebook took no action whatsoever to deal with the threat head-on. Facebook didn’t allocate time to investigate the threat level of the breach nor did Facebook evaluate whether or not it should notify users individually that their information was stolen.")
  
  elif topic.lower() == "c":
    print("I would convince victims to take action by filing a case for a cybersecurity breach. In reality, these actions take at least two years or more to make an impact. Therefore, my advice would be to enable two-factor authentication on all social media and personal accounts and change similar passwords to avoid falling victim to future breaches.")
    
  elif topic.lower() == "d":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  #input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")