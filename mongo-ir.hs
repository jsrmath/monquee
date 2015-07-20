module MongoIR where

type Object = [Pair]
type Identifier = String

data Command = Command Identifier Identifier [Item] deriving Show

data Item
	= LitItem Literal
	| ObjItem Object
	deriving Show

data Literal
	= String String
	| Int Int
	deriving Show

data Value
	= LitValue Literal
	| ObjValue Object
	deriving Show

data Pair = Pair Identifier Value deriving Show

data Token = TokenDB | TokenID String | TokenString String | TokenInt Int | TokenPipe | TokenComma
           | TokenSemi | TokenLBrace | TokenRBrace | TokenLBracket | TokenRBracket
           deriving Show