while True:

    # Takes string input of codons
    nuc = input("Enter query sequence.\n")

    transcribe_dict = {"a":"u","t":"a","g":"c","c":"g"}
    translate_dict = {"uuu":"Phe","uuc":"Phe","uua":"Leu",
    "uug":"Leu","cuu":"Leu","cuc":"Leu","cua":"Leu",
    "cug":"Leu","auu":"lle","auc":"lle","aua":"lle",
    "aug":"Met","guu":"Val","guc":"Val","gua":"Val",
    "gug":"Val","ucu":"Ser","ucc":"Ser","uca":"Ser",
    "ucg":"Ser","ccu":"Pro","ccc":"Pro","cca":"Pro",
    "ccg":"Pro","acu":"Thr","acc":"Thr","aca":"Thr",
    "acg":"Thr","gcu":"Ala","gcc":"Ala","gca":"Ala",
    "gcg":"Ala","uau":"Tyr","uac":"Tyr","uaa":"STOP",
    "uag":"STOP","cau":"His","cac":"His","caa":"Gln",
    "cag":"Gln","aau":"Asn","aac":"Asn","aaa":"Lys",
    "aag":"Lys","gau":"Asp","gac":"Asp","gaa":"Glu",
    "gag":"Glu","ugu":"Cys","ugc":"Cys","uga":"STOP",
    "ugg":"Trp","cgu":"Arg","cgc":"Arg","cga":"Arg",
    "cgg":"Arg","agu":"Ser","agc":"Ser","aga":"Arg",
    "agg":"Arg","ggu":"Gly","ggc":"Gly","gga":"Gly","ggg":"Gly"}


    transcribe_result = []
    translate_result = []

    for x in nuc.lower():
        transcribe_result.append(transcribe_dict[x])

    joined_transcript="".join(transcribe_result)
    print(f"\nYour queried sequence: {nuc}")
    print(f"\nQuery transcript: {joined_transcript}")

    #range(0,len(joined_transcript)-(3+len(joined_transcript)%3),3):

    for x in range(0,len(joined_transcript)-(3+len(joined_transcript)%3),3):
        translate_result.append(translate_dict[joined_transcript[x:x+3]])
    final= "-".join(translate_result)

    print(f"\nThe resulting amino acid sequence is: {final}\n")

    repeat = input("Another sequence? Y/N > ")
    while repeat not in ("Y","N"):
        repeat = input("Another sequence? Y/N > ")
    if repeat == "N":
        break
