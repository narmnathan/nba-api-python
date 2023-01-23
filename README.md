# SINIX
A model and data scraper for retrieving statistics on various NBA players. Basic statlines and advanced analytics are used to provide a strength rating that can be analyzed to determine player projections.
# Instructions
## First-Time Use
Load load.py and run functions load() and props() with the URL, Data_ID, and player name from basketball-reference. The Data_ID can be retrieved from inspecting the current row on basketball-reference.
!["Example of where to find Data ID"](https://i.imgur.com/h069j58.png)
A csv file will be loaded for you to import into an Excel spreadsheet with Power Query. Update the props() function to append new rows, and refresh the Power Query to update the spreadsheet.
