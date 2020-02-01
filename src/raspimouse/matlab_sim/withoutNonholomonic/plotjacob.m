%%
clf
close all
image_u = squeeze(us.Data).';
image_v = squeeze(vs.Data).';
%% timing
figure(666)
hold off
title('timing')
timing = 1000;
plot(image_u(timing:timing+50,:),image_v(timing:timing+50,:),'rx')
hold on
grid on

quiver(image_u(timing,:),image_v(timing,:),vuv.Data(timing,1:4),vuv.Data(timing,5:8))

%%
figure(6666)
hold off
for i = 1:100:size(tout,1)  
    for j = 1:4
    if (vuv.Data(i,j)*(image_u(i+1,j)-image_u(i,j)))>=0
        subplot(1,2,1)
        hold on
        plot(image_u(i,j),image_v(i,j),'ro') 
        subplot(1,2,2)
        hold on
        plot(xcar.Data(i,1),xcar.Data(i,2),'ro')         
    else
       subplot(1,2,1);hold on
       plot(image_u(i,j),image_v(i,j),'bx')
        subplot(1,2,2);hold on
        plot(xcar.Data(i,1),xcar.Data(i,2),'bx')         
    end
    end
end

    %image_v(i+1,:)-image_v(i,:);
figure(6667)
hold off
hold on
for i = 1:100:size(tout,1)
    for j = 1:4
    if (vuv.Data(i,j+4)*(image_v(i+1,j)-image_v(i,j)))>=0
       plot(image_u(i,j),image_v(i,j),'ro') 
    else
        plot(image_u(i,j),image_v(i,j),'bx')
    end
    end
end
