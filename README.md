
This program simulates a sports tournament, handling team selection, match results, and generating a standings table. Here’s a brief explanation of its functionality:

Initialization and Input:

The program starts by asking the user for the number of teams participating in the tournament.
It then offers the user a choice to enter team names manually or have them generated automatically from a predefined list.
Team Selection:

If the user chooses manual entry, they can input each team name.
If automatic selection is chosen, the program randomly selects team names from a predefined list.
Match Results:

The program asks the user whether they want to enter match results manually or have them generated automatically.
For manual entry, the user inputs the scores for each match.
For automatic generation, the program randomly assigns scores to matches.
Scoring and Statistics:

The program maintains dictionaries to track scores, goals scored, goals conceded, wins, losses, and draws for each team.
It updates these statistics based on match results.
Champion Announcement:

After all matches are processed, the program identifies and announces the team with the highest points as the champion.
Standings Table:

The program creates a table displaying team statistics, including points, matches played, wins, losses, draws, goals scored, goals conceded, and goal difference.
The table is sorted in descending order of points and saved to a CSV file.
Output:

The final standings table is printed, showing the rankings and statistics of all teams.
