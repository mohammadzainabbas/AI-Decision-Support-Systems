clear all
close all
load Dataset.mat
weights=zeros(1,9);
row=length(dataset);
prediction=zeros(row,1);
thresh=0.0;
lrate=0.1;
iter=1;
for k=1:iter
acc=0;
for i=1:row
    prod=dataset(i,1:9).*weights;
    if(sum(prod)>thresh)
        prediction(i)=1;
    else
        prediction(i)=0;   
    end
    error=lrate*(dataset(i,10)-prediction(i));
    weights=weights+dataset(i,1:9).*error;
end
accurate=row-sum(prediction-dataset(:,10));
accuracy=(accurate/row)*100;
disp('iteration'+string(k))
disp('accuracy: '+string(accuracy))
end
