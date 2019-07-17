<?php
use yii\helpers\Html;
use yii\widgets\ActiveForm;

$tests = Yii::$app->getRequest()->getQueryParam('tests');
$matrixDimension = Yii::$app->getRequest()->getQueryParam('matrixDimension');
$numberOfQuerys = Yii::$app->getRequest()->getQueryParam('numberOfQuerys');
?>
   
<h1> Tests:  <?php  echo $tests ?> </h1>
<p> Matrix Dimension:  <?php  echo $matrixDimension ?> </p>
<p> Number of Querys:  <?php  echo $numberOfQuerys ?> </p>


<?php

print '<form action="http://localhost:5000/" method="POST">';
foreach(range(1, $tests) as $T){
    print '<br> Test '.$T.'<br>';
    foreach(range(1, $numberOfQuerys) as $N){
        print ('<input type="text" name="text'.$T.$N.'"><br>');
        
    }
}
print '<input type="submit" name="Submit" value="Submit">';
print '</form>'
?>
