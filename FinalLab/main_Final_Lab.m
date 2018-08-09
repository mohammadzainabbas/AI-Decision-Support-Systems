function main()
%Load file
load('data.mat');
%Random sender nodes
Total_Sender_Nodes = round(100*(rand(1,1)));
%Generate random message

for i = 1:Total_Sender_Nodes
   n = round(rand(1,1)*100);
   message(i) = 2*sin(100*pi*n); 
end

%Generate modulated signal
for i = 1:length(message)
   modulated(i) = message(i)*cos(2*pi*3000*length(message(i))); 
end

%Add additive white gaussian noise to our modulated signal
snr = rand(1,1);
received = awgn(modulated,snr);

total_users = length(received);
total_samples = [];
for i = 1:length(received)
   total_samples = total_samples + length(received(i)); 
end

test_sample = [total_users, total_samples];
train_data = a(:,1:2);
train_labels = a(:,3);
size(train_data)
size(train_labels)


%Using KNN
model = fitcknn(train_data, train_labels);
model.NumNeighbors = 5;
predicted = predict(model, test_sample)



end

function Accuracy = Preceptron(data, labels, test)
weights=zeros(1,length(data));
row=length(data);
prediction=zeros(row,1);
thresh=0.0;
lrate=0.1;
iter=1;
for k=1:iter
acc=0;
for i=1:row
    prod=data(i,1:row).*weights;
    if(sum(prod)>thresh)
        prediction(i)=1;
    else
        prediction(i)=0;   
    end
    error=lrate*(data(i,row+1)-prediction(i));
    weights=weights+data(i,1:row).*error;
end
accurate=row-sum(prediction-labels);
accuracy=(accurate/row)*100;
disp('iteration'+string(k))
disp('accuracy: '+string(accuracy))
end
end

%KNN Classifier function

function accur = knnclassifier(traindata, testdata, K)

dist = zeros(size(traindata, 1), 1);
%Find distance with all training datapoints, sort and poll
for i = 1 : size(testdata)
x = testdata(i,:);
    
for j = 2 : size(traindata, 2)  
dist(:, 1) =  dist(:, 1) + (traindata(:, j) - x(j)) .^ 2;
end

dist(:, 1) = sqrt(dist(:, 1));
classes = train_labels;
dist(:, 2) = classes;
poll = sortrows(dist, 1);

%For tiebreak in case of even K
if (mod(K, 2) == 1)
expclass(i) = mode(poll(1 : K, 2));
else
    temp = poll(1 : K, 2);
    uniq = unique(temp);
    p = size(uniq);
    bincounts = histc(temp, uniq);
    q = max(bincounts);
    %if number of unique elements = 2 && highest frequency is K/2, then there is tie
    M = (p == 2) & (q == K/2);
    %Alloted the class which is at closest distance
    expclass(i) = mode(poll(1 : K - M, 2));    
end
end

%Error percentage calculation
error = transpose(expclass) - testdata(:, 1);
accur = ((size(error, 1) - nnz(error))/size(error, 1));

end