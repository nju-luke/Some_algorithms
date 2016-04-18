function Travel()    
    % 旅行商问题
    Location = randi(100,20,2); %产生城市坐标
    X = Location(:,1);
    Y = Location(:,2);

    T = 1000;  %初始化温度
    dt = 1;
    num = 10;       %在每一个T下发生多少次交换机会
    Dis_1 = distance(X,Y);
    k = T/100;
    Dis_best = inf;

    while T > 0
        for j = 1:num
            
            X_ex = X;
            Y_ex = Y;
            
            ex_1 = randi(20);   %生成交换坐标
            ex_2 = randi(20);
            
            X_ex(ex_1) = X(ex_2);X_ex(ex_2) = X(ex_1);  %生成交换后的序列
            Y_ex(ex_1) = Y(ex_2);Y_ex(ex_2) = Y(ex_1);
            
            Dis_ex = distance(X_ex,Y_ex);   %交换后的距离
            P = exp((Dis_1-Dis_ex)/k/T);    %求出交换距离变大时的接受概率
            
            if Dis_ex < Dis_1               %比较交换前后距离决定是否交换
                X = X_ex;
                Y = Y_ex;
                Dis_1 = Dis_ex;
                if Dis_1 < Dis_best         %保存最优位置，以免重新跳出来以后回不去          
                    X_best = X_ex;
                    Y_best = Y_ex;
                    Dis_best = Dis_ex;
                end
            elseif rand > P
                X = X_ex;
                Y = Y_ex;
                Dis_1 = Dis_ex;
            end
        end
    T = T-dt;                           %降温
    plot(X,Y)
    title(['distence=',num2str(Dis_1)])
    frame = getframe(gcf);
    end
    X_best = [0;X_best;0];
    Y_best = [0;Y_best;0];
    figure
    plot(X_best,Y_best)
    title(['distence=',num2str(Dis_best)])    
end

% function Dis = distance(X,Y)
%     length = size(X,1);
%     X1 = X(1:length-1);
%     Y1 = Y(1:length-1);
%     X2 = X(2:length);
%     Y2 = Y(2:length);
%     Dis = sqrt(sum((X1-X2).^2+(Y1-Y2).^2)); 
% end

function Dis = distance(X,Y)            %从坐标原点出发
    length = size(X,1);
    X1 = [0;X(1:length-1)];
    Y1 = [0;Y(1:length-1)];   
    Dis = sqrt(sum((X1-X).^2+(Y1-Y).^2)+X(length)^2+Y(length)^2); 
end