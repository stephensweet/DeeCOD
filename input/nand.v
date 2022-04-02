/* 
 Nand gate
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

   assign out = ~(a & b);
 
endmodule // nand_gate
