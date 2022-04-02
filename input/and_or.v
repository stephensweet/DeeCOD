/* 
 And then and or gate
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
   assign out = c | temp ;
 
endmodule // and_or_gate_system