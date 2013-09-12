import datetime

class DateTime():
    @staticmethod
    def malaysia_now():
        return datetime.datetime.utcnow() + datetime.timedelta(seconds=28800)
    
    @staticmethod
    def malaysia_today():
        now = datetime.datetime.utcnow() + datetime.timedelta(seconds=28800)
        return datetime.datetime(now.year, now.month, now.day)
    
    @staticmethod
    def is_date(date_string):
        result = None
        
        try:
            result = datetime.datetime.strptime(date_string, '%d/%m/%Y')
        except:
            pass
        
        if result is None:
            return False
        else:
            return True
    
    @staticmethod
    def to_date(date_string):
        return datetime.datetime.strptime(date_string, '%d/%m/%Y')
    
    @staticmethod
    def to_date_string(date2):
        if date2:
            return date2.strftime('%d/%m/%Y')
        else:
            return ''
    
    @staticmethod
    def to_time(time_string):
        return datetime.datetime.strptime(time_string, '%H:%M')
    
    @staticmethod
    def to_time_string(time2):
        if time2:
            return time2.strftime('%H:%M')
        else:
            return ''
    
    @staticmethod
    def to_time_string_12(time2):
        if time2:
            return time2.strftime('%I:%M %p')
        else:
            return ''
    
    @staticmethod
    def date_part(datetime2):
        return datetime.datetime(datetime2.year, datetime2.month, datetime2.day)
    
    @staticmethod
    def date_diff(interval, datetime_from, datetime_to):
        td = datetime_to - datetime_from
        
        if interval == 'day':
            return td.days
        else:
            return td.total_seconds()
        
class Bool():
    @staticmethod
    def to_bool(bool_str):
        if bool_str:
            if bool_str == 'true' or bool_str == 'yes' or bool_str == '1':
                return True
            else:
                return False
        else:
            return False
        
    @staticmethod
    def to_string(bool2):
        return 'Yes' if bool2 == True else 'No'
    
class Money():
    @staticmethod
    def to_word(amt, currency_name, currency_cent):
        s = ''
        str = '%.2f' % amt
        cent = "%s" % Money.__to_word_2d(int(str[len(str) - 2:]), True);
        str = str[0: str.Length - 3];

        # get ringgit
        s2 = ''
        d3 = ""
        level = 0;
        while len(str) > 0:
            s2 = ''

            if len(str) > 3:
                d3 = str[str.Length - 3:]
                str = str[0: str.Length - 3]
            else:
                d3 = str
                str = ""

            level += 1

            s2 += "%s" % Money.__to_word_3d(int(d3))

            if level == 1:
                s2 += ""
            elif level == 2:
                s2 += " Thousand"
            elif level == 3:
                s2 += " Million"
            elif level == 4:
                s2 += " Billion"
            elif level == 5:
                s2 += " Trillion"
            elif level == 6:
                s2 += " Quadrillion"
            elif level == 7:
                s2 += " Quintillion"
            elif level == 8:
                s2 += " Sextillion"
            elif level == 9:
                s2 += " Septillion"
            elif level == 10:
                s2 += " Octillion"
            else:
                s2 += " Unknown"

            if len(s) > 0:
                s = " " + s
            s = s2 + s

        s = " " + s
        s = currency_name + s

        if len(cent) > 0:
            s += " and %s %s" % (currency_cent, cent)

        if len(s) > 0:
            s += " Only"

        return s
    
    @staticmethod
    def __to_word_3d(d):
        s = ''

        i = int(d / 100)
        if i > 0:
            s += "%s Hundred" % Money.__to_word_1d(i, True)
            d -= i * 100

        if len(s) > 0:
            s += " %s" % Money.__to_word_2d(d, True)
        else:
            s += "%s" % Money.__to_word_2d(d, False)

        return s
        
    @staticmethod
    def __to_word_2d(d, skipZero):
        if skipZero and d == 0:
            return ""
        
        if d < 0:
            return ""

        s = ''

        if d < 10:
            s += Money.__to_word_1d(d, skipZero)
        elif d == 10:
            s += "Ten"
        elif d == 11:
            s += "Eleven"
        elif d == 12:
            s += "Twelve"
        elif d == 13:
            s += "Thirteen"
        elif d == 14:
            s += "Fourteen"
        elif d == 15:
            s += "Fifteen"
        elif d == 16:
            s += "Sixteen"
        elif d == 17:
            s += "Seventeen"
        elif d == 18:
            s += "Eighteen"
        elif d == 19:
            s += "Nineteen"
        else:
            i = int(d / 10);
            if i == 2:
                s += "Twenty"
            elif i == 3:
                s += "Thirty"
            elif i == 4:
                s += "Forty"
            elif i == 5:
                s += "Fifty"
            elif i == 6:
                s += "Sixty"
            elif i == 7:
                s += "Seventy"
            elif i == 8:
                s += "Eighty"
            elif i == 9:
                s += "Ninety"

            d -= i * 10;
            d1 = Money.__to_word_1d(d, True)
            if len(d1) > 0:
                s += "-"
            s += d1

        return s
        
    @staticmethod
    def __to_word_1d(i, skipZero):
        if skipZero and i == 0:
            return ''
            
        if i < 0:
            return ''

        s = ''
        if i == 1:
            s += "One"
        elif i == 2:
            s += "Two"
        elif i == 3:
            s += "Three"
        elif i == 4:
            s += "Four"
        elif i == 5:
            s += "Five"
        elif i == 6:
            s += "Six"
        elif i == 7:
            s += "Seven"
        elif i == 8:
            s += "Eight"
        elif i == 9:
            s += "Nine"
        elif i == 0:
            s += "Zero"

        return s