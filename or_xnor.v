/* 
 or then and xnor gate
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

   assign temp = a | b;
   assign out = ~(temp ^ c);
 
endmodule // 