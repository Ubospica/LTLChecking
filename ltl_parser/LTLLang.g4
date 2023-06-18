grammar LTLLang;

// we use ! for ¬, /\ for conjunction, \/ for disjunction, −> for implication, X for next, G for
// always, F for eventually, and U for until. You can assume enough brackets to eliminate ambiguity

formula:
	'!' formula								# not_formula
	| 'G' formula							# g_formula
	| 'F' formula							# f_formula
	| 'X' formula							# x_formula
	| <assoc = right> formula 'U' formula	# u_formula
	| formula op = (AndOp | OrOp) formula	# logic_formula
	| formula '->' formula					# implication_formula
	| logicConstant							# logic_const
	| Identifier							# atomic_proposition
	| '(' formula ')'						# formula_in_parentheses;

logicConstant: true_literal | false_literal;

Identifier: [a-z]+;

AndOp: '/\\';

OrOp: '\\/';

true_literal: 'true';

false_literal: 'false';

WS: [ \t\n\r]+ -> skip;
