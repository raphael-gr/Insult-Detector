<h1>Insult Detector</h1>
    <h2>Summary</h2>
         <p>
            The aim of this project is to provide an efficient and easy-to-use app to flag out tweets that contain insults. This tool will prove handy for moderation.</br>
            <b>Only English is currently implemented.</b> This means this app cannot process tweets in any other language.
        </p>
        </br>
        ![Screenie](https://i.imgur.com/F2ZLc7B.png "Screenshot")
    <h2>Features</h2>
        <ul>
                <h3>Detect insults within replies to a tweet</h3>
                    <p>
                        Profanity words check, filter evading check, polarity analysis with NLP.
                    </p>
                <h3>Detect insults within a stream related to keywords</h3>
                    <p>
                        Start and stop the stream anytime, get live feedback. Profanity words check.
                    </p>
                <h3>Detect insults within results from a standard twitter query</h3>
                    <p>
                        Profanity words check, filter evading check, polarity analysis with NLP.
                    </p>
                <h3>Dictionary editing</h3>
                    <p>
                        Twinsult's main detector looks for insults in an insult dictionary. It features smart tools to
                        edit the dictionary in-program.</br>
                        You may also download dictionaries from the internet for more specific filters.
                    </p>
    <h2>Project's origin</h2>
        <p>
            This project was created for CentraleSupélec's coding weeks, a two-week long bootcamp which aims, through the realization of computer development projects, to allow students to consolidate their knowledge in programming and development of computer applications on the one hand and on the other hand to learn about the practices and methodologies of group computer development. </br>
            If you have access to edunao, you may <a href="https://centralesupelec.edunao.com/course/view.php?id=1214">see more here.</a>
        </p>
    <h2>Structure</h2>
        <p>
            Root folder includes __main__.py, which is the only function you should call, a src folder which includes whole source code,
            and a tests folder. </br>
            Source follows architecture:
            <ul>
                <li> 
                    collection package: modules making requests to TwitterAPI using tweepy
                </li>
                <li>
                    data package: contains insults' dictionary and a small script to process it
                </li>
                <li>
                    GUI package: modules pertaining to the interface, using tkinter and using OOP.
                </li>
                <li>
                    Essential functional modules: 
                        <ul>
                            <li>
                                detect.py: contains functions detecting whether tweets are insulting.
                            </li>
                            <li>
                                distance.py: checks if words are close to insults, which may be "filter evading".
                            </li>
                        </ul>
                </li>
                <li>
                    A couple of small, explicit scripts.
                </li>
            </ul>
        </p>
    <h2>Installation</h2>
        <p>
            Simply clone this project from github using command: <br/>
            git clone &#60https clone link for the repository&#62  <br/>
            Then run __main__.py.
        </p>
    <h3> Libraries required </h3>
        <p>
            pytest (5.2.2) ; tweepy (3.8.0) ; nltk (3.4.5) ; textblob (0.15.3) ; ttkthemes:  2.4.0. </br>
            GUI uses library tkinter, which is native in Python.
        </p>
    <h2>License</h2>
        <p>None yet.</p>