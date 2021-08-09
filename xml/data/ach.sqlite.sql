BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "trx" (
	"MsgId"	TEXT,
	"InstrId"	text,
	"EndToEndId"	text,
	"TxId"	text,
	"IntrBkSttlmAmt"	text,
	"IntrBkSttlmCcy"	TEXT,
	"ChrgBr"	text,
	"DbtrNm"	text,
	"DbtrAcctId"	TEXT,
	"DbtrAgtBIC"	TEXT,
	"DbtrAgtBrnchId"	TEXT,
	"CdtrAgtBIC"	text,
	"CdtrAgtBrnchId"	text,
	"CdtrNm"	text,
	"CdtrAcctId"	TEXT,
	"CdtrAcctTp"	Text,
	"Purp"	Text,
	"RmtInfUstrd"	Text,
	PRIMARY KEY("MsgId","InstrId")
);
CREATE TABLE IF NOT EXISTS "GrpHdr" (
	"pacs_type"	TEXT,
	"MsgId"	TEXT,
	"CreDtTm"	TEXT,
	"NbOfTxs"	TEXT,
	"TtlIntrBkSttlmAmt"	TEXT,
	"TtlIntrBkSttlmCcy"	TEXT,
	"IntrBkSttlmDt"	TEXT,
	"SttlmMtd"	TEXT,
	"ClrSysId"	TEXT,
	"InstrPrty"	TEXT,
	"ClrChanl"	TEXT,
	"CtgyPurp"	TEXT,
	PRIMARY KEY("MsgId")
);
CREATE TABLE IF NOT EXISTS "pacs_004" (
	"MsgId"	TEXT,
	"OrgnlMsgId"	TEXT,
	"OrgnlMsgNmId"	TEXT,
	"RtrRsn"	TEXT,
	"TrxRtrId"	TEXT,
	"OrgnlEndToEndId"	TEXT,
	"GrpSts"	TEXT,
	"OrgnlTxId"	TEXT,
	"RtrdIntrBkSttlmAmt"	TEXT,
	"RtrdIntrBkSttlmCcy"	TEXT,
	PRIMARY KEY("MsgId","OrgnlMsgId")
);
COMMIT;
