/* 
 Xnor gate
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

   assign out = ~(a ^ b);
 
endmodule // xnor_gate