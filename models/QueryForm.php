<?php

namespace app\models;

use Yii;
use yii\base\Model;

class QueryForm extends Model
{
    public $querys;

    public function rules()
    {
        return [
            ['querys', 'required']
        ];
    }
}