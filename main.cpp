
#include <iostream>
#include <string>

#include "exprtk.hpp"

using SymbolTable = exprtk::symbol_table<long double>;
using Expression  = exprtk::expression<long double>;
using Parser      = exprtk::parser<long double>;

int main()
{
  using std::cout;
  using std::endl;
  using std::string;

  using namespace std::string_literals;


  auto expression_string = "x^2 + 32 - 4"s;
  long double x{320};

  SymbolTable symbol_table;
  symbol_table.add_variable("x", x);
  symbol_table.add_constants();

  Expression expression;
  expression.register_symbol_table(symbol_table);

  Parser parser;

  parser.compile(expression_string, expression);

  cout << expression.value() << endl;
}

// vim:set et ts=2 sw=2 sts=2:

