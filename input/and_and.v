/* 
 and then and and gate
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
 	input c;

	output out;

	wire temp;

   assign temp = a & b;
   assign out = c & temp);
 
endmodule // 