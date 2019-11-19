accounts = {}
                    filename = 'accounts.txt'
                    accounts[str(entry_new_pass.get())] = str(entry_new_pass2.get())
                    file = open(filename, 'ab')
                    pickle.dump(accounts, file)
                    file.close()



