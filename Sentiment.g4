grammar Sentiment;

// Ngữ pháp chỉ xử lý câu đơn, hiện tại đơn, chưa xử lý được các ngữ pháp phức tạp hơn
program: statement;

statement
    : statement1 // Cảm nhận của người dùng, e.g: I like this product.
    | statement2 // Bản chất sản phẩm, dịch vụ, e.g: The product is amazing.
    ;

statement1
    : (subj)? verb obj
    ;


subj
    : 'i' | 'you' | 'we'
    ;

verb
    : neu_v | pos_v | neg_v
    ;

neu_v
    : 'understand' | 'know' | 'recognize'
    ;

pos_v
    : 'like' | 'love' | 'enjoy' | 'good'
    ;

neg_v
    : 'hate' | 'dislike' | 'despise'
    ;

article
    : 'the' | 'an' | 'a'
    ;

pronoun
    : 'this' | 'that' | 'there' | 'those' 
    ;

obj
    : (article)? (pronoun | STRING)+
    ;

statement2
    : noun state_verb description_phrase
    ;

noun
    : (article | pronoun)? STRING
    ;


state_verb
    : 'is' | 'are' | 'seems' | 'look' | 'feels' | 'seem' | 'feel' | 'looks'
    ;

description_phrase
    : (neu_ph | pos_ph | neg_ph)
    ;

neu_ph
    : 'average' | 'normal' | 'mediocre'
    ;

pos_ph
    : 'good' | 'amazing' | 'excellent' | 'wonderful' | 'fantastic'
    ;

neg_ph
    : 'bad' | 'horrible' | 'boring' | 'terrible'
    ;

//Token
STRING
    : [a-zA-Z]+
    ;

WS : [ \t\r\n]+ -> skip;
