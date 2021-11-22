//all the quotes in array of strings.
var quotes = ["I dont think a tough question is disrespectful.
― Helen Thomas",
 "“The man who reads nothing at all is better educated than the man who reads nothing but newspapers.”
― Thomas Jefferson",
"“Myth is much more important and true than history. History is just journalism and you know how reliable that is.”
― Joseph Campbell",
"“I believe in equality for everyone, except reporters and photographers.”
― Mahatma Gandhi",
"“You're miserable, edgy and tired. You're in the perfect mood for journalism.”
― Warren Ellis",
"“Journalism largely consists in saying ,Lord Jones is dead, to people who never knew Lord Jones was alive.”
― G.K. Chesterton",
"“Better a good journalist than a poor assassin.”
― Jean-Paul Sartre",
"“By giving us the opinions of the uneducated, journalism keeps us in touch with the ignorance of the community.”
― Oscar Wilde",
"“Freedom of speech gives us the right to offend others, whereas freedom of thought gives them the choice as to whether or not to be offended.”
― Mokokoma Mokhonoana",
"“American journalism (like the journalism of any other country) is predominantly paltry and worthless. Its pretensions are enormous, but its achievements are insignificant.”
― H. L. Mencken"]

//function for new quotes and for random picking.
function Quote(){
    var ranInt = Math.floor(Math.random() * (quotes.length));
    document.getElementById("nquote").innerHTML = quotes[ranInt];
}