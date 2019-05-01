function [u,v,z,valid]=projection(X,OBJ,K)
%%%%%%%
% X = [xc,yc,thetac] 
% OBJ = [xo,yo,zo]
%%%%%%
% assert size(X,1) == 3
% assert size(X,2) == 1
% assert size(K,1) == 3
% assert size(K,2) == 3
% assert size(OBJ,1) == 3
% assert size(OBJ,2) == 1

%%%%%
% conversion
% todo
%%%%%



%%%%%
% Rotate to camera 
%%%%%
Cta = X(3);
Rinv = [cos(Cta),sin(Cta);-sin(Cta),cos(Cta)];
X_c = Rinv*(OBJ(1:2,1)-X(1:2,1));
x_c = -X_c(2);
y_c=OBJ(3);
z_c = X_c(1);

if z_c == 0
    u = 0;
    v = 0;
    z = 0;
    valid = 0;
    return;
end
imagepoints=K*[x_c/z_c;y_c/z_c;1];

u = imagepoints(1);
v = imagepoints(2);
z = z_c;
valid = 1;


end