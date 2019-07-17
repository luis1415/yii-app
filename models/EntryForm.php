<?php

namespace app\models;

use Yii;
use yii\base\Model;

class EntryForm extends Model
{
    public $tests;
    public $matrixDimension;
    public $numberOfQuerys;

    public function rules()
    {
        return [
            ['tests', 'required'],
            ['tests', 'integer', 'min' => 1], 
            ['tests', 'integer', 'max' => 50],
            ['matrixDimension', 'required'],
            ['matrixDimension', 'integer', 'min' => 1], 
            ['matrixDimension', 'integer', 'max' => 100],
            ['numberOfQuerys', 'required'],
            ['numberOfQuerys', 'integer', 'min' => 1], 
            ['numberOfQuerys', 'integer', 'max' => 1000]
        ];
    }
}