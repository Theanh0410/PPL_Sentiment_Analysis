grammar Sentiment;

program: statement;

statement: statement1 | statement2 ;

statement1  : (subject)? verb obj ;

subject     : 'i' | 'you' | 'we' ;

verb: neu_v | pos_v | neg_v;

neu_v: 'understand' | 'know' | 'recognize';

pos_v: 'like' | 'love' | 'enjoy';

neg_v: 'hate' | 'dislike' | 'despise';

obj: STRING*;

statement2: noun description_phrase;

noun: STRING*;

description_phrase: neu_ph | pos_ph | neg_ph;

neu_ph: 'average' | 'normal' | 'mediocre';
pos_ph: 'good' | 'amazing' | 'excellent' | 'wonderful' | 'fantastic';
neg_ph: 'bad' | 'horrible' | 'boring' | 'terrible';

// Lexer 
STRING : [a-zA-Z]+ ;
WS : [ \t\r\n]+ -> skip ;

