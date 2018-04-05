# prepare_data_4knn
This file is uesd to process some data for myself. <br>
It also a kind of practice for new guy for Python. <br>
I want to organise 10 prices from each file in sample directory as a set and get the changes (There will be 9 changes) and put those changes into a new file. Which will be used for KNN algorithm (which is not showed int this programme).

At first I tested in dir 'test'. Coded in 'process_data_4knn.py'. Put result into 'result.csv' file.

Then I used 'process_data_4knn_do.py' to do the actual word. The final result is in 'all_stockschanges_5yr.csv'.

After thar, I tail last 9 lines from each files of 'individual_stocks_5yr' and write them into seperate file for each. Used shell is 'tail8lines.sh' in 'prepare_9days_data'.

Then I need to create price changes for those 9 days data. 
