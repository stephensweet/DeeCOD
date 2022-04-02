/* 
 or then and not gate
*/
module gatedesign
(
 a,
 b,
 out
 );

	input a;
	input b;
	input c;

	output out;

	wire temp;

   assign temp = a | b;
   assign out = ~(temp);
 
endmodule // 