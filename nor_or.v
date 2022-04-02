/* 
 nor , not circuit
*/
module gatedesign
(
 a,
 b,
 out
 );

	input a;
	input b;

	output out;

	wire temp;

   assign temp = ~(a | b);
   assign out = ~temp;
 
endmodule // 