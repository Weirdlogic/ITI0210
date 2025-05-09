% Geography Facts (Direct Paths)
% East Relationships
east(mordor,gondor).
east(gondor,rohan).
east(rohan,lothlorien).
east(lothlorien,moria).
east(moria,high_pass).
east(high_pass,rivendell).
east(rivendell,bree).
east(bree,shire).

% South Relationships
south(mordor,gondor).
south(gondor,rohan).
south(rohan,lothlorien).
south(lothlorien,moria).
south(moria,high_pass).
south(high_pass,rivendell).
south(rivendell,bree).
south(bree,shire).

% Basic Transitivity Rules
-east(X,Y) | -east(Y,Z) | east(X,Z).
-south(X,Y) | -south(Y,Z) | south(X,Z).

% Symmetry Rules
-east(X,Y) | west(Y,X).
-south(X,Y) | north(Y,X).

% Proof Queries

% Proof that Mordor is east of the Shire
-east(mordor,shire) | $ans(east).

% Proof that Mordor is south of the Shire
-south(mordor,shire) | $ans(south).

% Southeast Definition
-east(X,Y) | -south(X,Y) | southeast(X,Y).

% Proof that Mordor is southeast of the Shire
-east(mordor,shire) | -south(mordor,shire) | southeast(mordor,shire).
-southeast(mordor,shire) | $ans(southeast).

% Proof that Mordor is NOT west or north of the Shire
-west(mordor,shire) | $ans(not_west).
-north(mordor,shire) | $ans(not_north).
