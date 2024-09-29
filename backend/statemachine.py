from datetime import datetime

class UserStateMachine:
    
    
    def __init__(self):
        self.currentState = 0
        self.dialogueEnded = False
        self.questions = [
        {
            "id": "goal",
            "question": "What would you like to do?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },

        {
            "id": "kodurzadu",
            "question": "Piękna odpowiedź!\nCzy możesz podać swój kod urzadu?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },

         {
            "id": "pesel",
            "question": "Piękna odpowiedź!\nCzy możesz podać swój pesel?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },

         {
            "id": "name",
            "question": "Piękna odpowiedź!\nCzy możesz podać swóje imie?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },

         {
            "id": "surname",
            "question": "Piękna odpowiedź!\nCzy możesz podać swóje nazwisko?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },

         {
            "id": "dateofbirth",
            "question": "Piękna odpowiedź!\nCzy możesz podać swóju datu narodzenia?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },

         {
            "id": "countrycode",
            "question": "Piękna odpowiedź!\nTeraz musimy wypełnić twój adres\nCzy możesz podać swój country code?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },

         {
            "id": "wojewodztwo",
            "question": "Piękna odpowiedź!\nTeraz musimy wypełnić twój adres\nCzy możesz podać swóje wojewodztwo?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },

         {
            "id": "powiat",
            "question": "Piękna odpowiedź!\nTeraz musimy wypełnić twój adres\nCzy możesz podać swój powiat?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },

         {
            "id": "gmina",
            "question": "Piękna odpowiedź!\nTeraz musimy wypełnić twój adres\nCzy możesz podać swóju gminu?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },

         {
            "id": "ulica",
            "question": "Piękna odpowiedź!\nTeraz musimy wypełnić twój adres\nCzy możesz podać swóju ulicu?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },

         {
            "id": "nrdomu",
            "question": "Piękna odpowiedź!\nTeraz musimy wypełnić twój adres\nCzy możesz podać swój nr. domu?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },

         {
            "id": "nrlockalu",
            "question": "Piękna odpowiedź!\nTeraz musimy wypełnić twój adres\nCzy możesz podać swój nr. lockalu?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },

         {
            "id": "miejscowosc",
            "question": "Piękna odpowiedź!\nTeraz musimy wypełnić twój adres\nCzy możesz podać swóju miejscowosc?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },

         {
            "id": "zipcode",
            "question": "Piękna odpowiedź!\nTeraz musimy wypełnić twój adres\nCzy możesz podać swój kod pocztowy?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },

         {
            "id": "price",
            "question": "Piękna odpowiedź!\nTeraz musimy wypełnić twój adres\nCzy możesz podać swój dochod?",
            "validation": lambda value: True,
            "errorMessage": "Can you please give a normal answer?",
            "userReply": ""
        },
        ]

    def getQuestionForId(self, questionId):
        for q in self.questions:
            # print("q[id] is ", q['id'])
            if q['id'] == questionId:
                return q

        # print("getQuestionForId() asked for ", questionId)
        return self.questions[0] # just in case, shouldnt be here

    def restartStates(self):
        self.currentState = 0


    def getCurrentQuestion(self):
        return self.questions[self.currentState]

    # invoked by the user when he answers a question
    def handleUserResponse(self, reply):
        retMsg = ""
        if self.questions[self.currentState]['validation'](reply):
            self.questions[self.currentState]['userReply'] = reply
            self.currentState += 1

        else:
            retMsg = self.questions[self.currentState]['errorMessage']

        if self.currentState >= len(self.questions):
            print("we're done!")
            # we're done
            self.generateXml(datetime.today().strftime('%Y-%m-%d', ),
            self.getQuestionForId("kodurzadu")["userReply"],
            self.getQuestionForId("pesel")["userReply"],
            self.getQuestionForId("name")["userReply"],
            self.getQuestionForId("surname")["userReply"],
            self.getQuestionForId("dateofbirth")["userReply"],
            self.getQuestionForId("countrycode")["userReply"],
            self.getQuestionForId("wojewodztwo")["userReply"],
            self.getQuestionForId("powiat")["userReply"],
            self.getQuestionForId("gmina")["userReply"],
            self.getQuestionForId("ulica")["userReply"],
            self.getQuestionForId("nrdomu")["userReply"],
            self.getQuestionForId("nrlockalu")["userReply"],
            self.getQuestionForId("miejscowosc")["userReply"],
            self.getQuestionForId("zipcode")["userReply"],
            self.getQuestionForId("goal")["userReply"],
            self.getQuestionForId("price")["userReply"],

            )
            retMsg = "Dzięki za odpowiedź! Oto twój link xml: ...<a href='taxform.xml'>link</a>. Pamiętaj, aby przesłać je na naszą stronę internetową!"
            self.dialogueEnded = True

        else:
            retMsg = self.questions[self.currentState]['question']


        return retMsg

    def generateXml(self, date, kodurzadu, pesel, name, surname, dateofbirth,
    countrycode, wojewodztwo, powiat, gmina, ulica, nrdomu, nrlockalu, miejscowosc,
    zipcode, goal, price):
        xmlText = """<?xml version="1.0" encoding="UTF-8"?>
<Deklaracja xmlns="http://crd.gov.pl/wzor/2023/12/13/13064/">
<Naglowek>
<KodFormularza kodSystemowy="PCC-3 (6)" kodPodatku="PCC" rodzajZobowiazania="Z" wersjaSchemy="1-0E">PCC-3</KodFormularza>
<WariantFormularza>6</WariantFormularza> 
<CelZlozenia poz="P_6">1</CelZlozenia> 
<Data poz="P_4">{date}</Data> 
<KodUrzedu>{kodurzadu}</KodUrzedu>
</Naglowek>
<Podmiot1 rola="Podatnik">
<OsobaFizyczna>
<PESEL>{pesel}</PESEL>
 <ImiePierwsze>{name}</ImiePierwsze>
  <Nazwisko>{surname}</Nazwisko> 
  <DataUrodzenia>{dateofbirth}</DataUrodzenia>
</OsobaFizyczna>
<AdresZamieszkaniaSiedziby rodzajAdresu="RAD">
<AdresPol>
<KodKraju>{countrycode}</KodKraju> 
<Wojewodztwo>{wojewodztwo}</Wojewodztwo> 
<Powiat>{powiat}</Powiat> 
<Gmina>{gmina}</Gmina> 
<Ulica>{ulica}</Ulica> 
<NrDomu>{nrdomu}</NrDomu> 
<NrLokalu>{nrlockalu}</NrLokalu> 
<Miejscowosc>{miejscowosc}</Miejscowosc> 
<KodPocztowy>{zipcode}</KodPocztowy>
</AdresPol> </AdresZamieszkaniaSiedziby>
</Podmiot1> <PozycjeSzczegolowe>
<P_7>2</P_7>
<P_20>1</P_20> 
<P_21>1</P_21> 
<P_22>1</P_22> 
<P_23>{goal}</P_23> 
<P_24>{price}</P_24> 
<P_25>100</P_25> 
<P_46>100</P_46> 
<P_53>100</P_53> 
<P_62>1</P_62>
</PozycjeSzczegolowe>
<Pouczenia>1</Pouczenia> 
</Deklaracja>
        """.format(date=date, kodurzadu=kodurzadu, pesel=pesel, name=name, surname=surname, dateofbirth=dateofbirth,
    countrycode=countrycode, wojewodztwo=wojewodztwo, powiat=powiat, gmina=gmina, ulica=ulica, nrdomu=nrdomu, nrlockalu=nrlockalu, miejscowosc=miejscowosc,
    zipcode=zipcode, goal=goal, price=price)

        self.xmlText = xmlText

        return xmlText
