/* 
 not, nor circuit
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

   assign temp = ~a;
   assign out = ~(b | temp);
 
endmodule // 