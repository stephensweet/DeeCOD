/* 
 and then and not gate
*/
module gatedesign
(
 a,
 b,
 c,
 out
 );

	input a;
	input b;

	output out;

	wire temp;

   assign temp = a & b;
   assign out =  ~temp;
 
endmodule // 