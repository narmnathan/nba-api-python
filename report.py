import os
from datetime import date
from load import load
import maintest
from variables import CSV, filters
from filters import homecourt, opponent, last, min, without
from stats import basic, reb_type, fg_type, tm_advanced, opp_advanced


# to-do: properly connect load -> filters -> stats! markdown reports showing stats for anthony davis...
# take load function and print header to document
def report():
    dict = CSV.vars
    player = str(dict[0]) + " " + str(dict[1])
    team = dict[2]
    court = dict[3]
    opp = dict[4]
    prop_num = dict[5]
    prop_type = dict[6]
    # open markdown file
    today = date.today()
    title = player + ' ' + prop_num + ' ' + prop_type + ' ' + today.strftime("%m-%d-%y")

    md_path = os.getcwd() + '/reports/md/' + title + '.md'
    report = open(md_path, "w+")

    # new-line function
    def newline():
        report.write("\n\n")

    # write header and confirm load
    header1 = player + ', ' + team + ' ' + court + ' ' + opp + ', ' + prop_num + ' ' + prop_type
    report.write("# " + header1)
    report.write("\n\n")
    report.write('---')
    report.write("\n\n")

    # function to load main stats
    def basic_load():
        report.write(basic())
        newline()
        report.write(reb_type())
        newline()
        report.write(fg_type())
        newline()

    # function to reset gamelog
    def reset():
        load(player, team, court, opp, prop_num, prop_type)

    # season stats
    header2 = "## Season:"
    report.write(header2)
    newline()
    basic_load()

    # last 10 games stats
    header3 = "## Last 10 games:"
    report.write(header3)
    newline()
    last(10)
    basic_load()
    reset()

    # court-filtered stats
    if court == '@':
        homecourt('AWAY')
        header4 = "## In away games:"
        report.write(header4)
        newline()
        basic_load()
        reset()
    elif court == 'vs.':
        homecourt('HOME')
        header4 = "## In home games:"
        report.write(header4)
        newline()
        basic_load()
        reset()

    # opponent-filtered stats
    header5 = "## Against " + opp + ":"
    report.write(header5)
    newline()
    opponent(opp)
    basic_load()
    reset()

    # advanced stats
    header6 = "## Advanced season stats:"
    report.write(header6)
    newline()
    report.write(tm_advanced())
    newline()
    report.write(opp_advanced())
    newline()

    # convert md to pdf
    file = title + '.md'
    # pdf_path = os.getcwd() + '/reports/pdf/' + title + '.pdf'
    # os.system('mdpdf -o ' + pdf_path + ' ' + file)

    # final
    print("'" + file + "'" + ' successfully created')


report()

# to-do: rewrite report module and break up into pieces.
# filter and stats modules have to work together in that filter has to provide the gamelogs and stats have to retrieve the stats,
# so writing has to be done modularly.