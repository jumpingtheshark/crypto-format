class CryptoFormatter:
    def parse_input_string(self, input_string):
        input_list = input_string.split(',')
        message = input_list[0]
        pad_size = int(input_list[1])
        return message, pad_size

    def cformat(self, message, pad_size):
        mc = list(message)
        j = len(mc)
        sl = []  # shadowlist

        for i in range(0, j):
            if (mc[i] != '.' and mc[i] != ':') or i == 0:
                if (str(mc[i]).isdigit()):
                    sl.append(0)
                else:
                    sl.append(1)
            else:
                if (mc[i - 1].isdigit() and mc[i + 1].isdigit()):
                    sl.append(0)
                else:
                    sl.append(1)

        j = len(sl)
        splitpoints = []
        splitpoints.append(0)

        for i in range(1, j):
            cur_type = sl[i]
            prev_type = sl[i - 1]
            if (cur_type != prev_type):
                splitpoints.append(i)

        splitpoints.append(j)

        # print(splitpoints)

        tokens = []

        for i in range(0, len(splitpoints) - 1):
            start = splitpoints[i]
            end = splitpoints[i + 1]
            token = message[start:end]
            tokens.append(token)

        # now walk through the tokens and pad if it's a number
        # print(tokens)
        padded_tokens = []
        offset = 0
        for t in tokens:
            try:
                float(t)
                i = t.find('.')
                if i > -1:
                    offset = len(t)-i
                pad_size = pad_size + offset
                t = t.zfill(pad_size)
                #print("padded", t)
                padded_tokens.append(t)
            except ValueError:
                print("")
                padded_tokens.append(t)

        print(padded_tokens)

        # finally stitch the string backup
        s = ""
        for t in padded_tokens:
            s = s + str(t)

        # print(s)
        return s
