/* 
 nand, xor, not circuit
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

   assign temp = ~(a & b);
   assign temp1 = temp ^ c;
   assign out = ~temp1;
 
endmodule // 